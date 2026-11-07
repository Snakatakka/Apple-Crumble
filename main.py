from parser import parse_tag, parse_contents
from converter import convert_to_html

def main():
    with open("test.md") as file:
        for line in file:
            tag = parse_tag(line)
            contents = parse_contents(line, tag)
            print(convert_to_html(contents, tag))
            
main()