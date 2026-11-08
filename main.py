from parser import parse_tag, parse_contents
from converter import convert_lines_to_html, convert_contents_to_html

def main():
    with open("test.md") as file:
        with open("test.html", "w") as html_file:
            html_file.write("<body> \n")
            for line in file:
                if line.startswith("<") or line.strip("\n").endswith(">"):
                    html_file.write(line) # Skips the whole shebang if the line is already in html
                else:
                    tag = parse_tag(line)
                    contents = parse_contents(line, tag)
                    html_contents = convert_contents_to_html(contents)
                    print(html_contents)
                    converted_line = convert_lines_to_html(html_contents, tag)
                    html_file.write(f"{converted_line} \n")
            html_file.write("</body>")
            
main()