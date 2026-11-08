from parser import parse_tag, parse_contents
from converter import convert_lines_to_html, convert_contents_to_html

def main():
    with open("test.md") as file:
        html_file = open("test.html", "w")
        html_file.write("<body> \n")
        for line in file:
            tag = parse_tag(line)
            contents = parse_contents(line, tag)
            html_contents = convert_contents_to_html(contents)
            converted_line = convert_lines_to_html(html_contents, tag)
            html_file.write(f"{converted_line} \n")
        html_file.write("</body")
        html_file.close()
            
main()