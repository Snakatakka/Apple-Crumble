from parser import parse_tag, parse_contents
from converter import convert_lines_to_html, convert_contents_to_html
import os
import yaml

def init():
   os.mkdir("_content")
   os.mkdir("_static")
   os.mkdir("_site")
   make_page("index")

def make_page(page_name : str):
    os.mkdir(f"_content/{page_name}")
    open(f"_content/{page_name}/{page_name}.md", "w")
    open(f"_content/{page_name}/{page_name}.yaml", "w")

def build(file_name : str):
    with open(f"_content/{file_name}/{file_name}.yaml") as yaml_file:
        yaml.load(yaml_file, yaml.FullLoader)
        with open(f"_content/{file_name}/{file_name}.md") as md_file:
            os.mkdir(f"_site/{file_name}")
            with open(f"_site/{file_name}/{file_name}.html", "w") as html_file:
                html_file.write("<!DOCTYPE html>\n<html>\n")
                html_file.write("<head>\n")
                html_file.write("<meta charset=\"UTF-8\">\n")
                html_file.write("</head>\n")
                html_file.write("<body>\n")

                for line in md_file:
                    if line.startswith("<") or line.strip("\n").endswith(">"):
                        html_file.write(line) # Skips the whole shebang if the line is already in html
                    else:
                        tag = parse_tag(line)
                        contents = parse_contents(line, tag)
                        html_contents = convert_contents_to_html(contents)
                        converted_line = convert_lines_to_html(html_contents, tag)
                        html_file.write(f"{converted_line} \n")
            
                html_file.write("</body>\n")
                html_file.write("</html>")
            
init()
make_page("test")
build("test")