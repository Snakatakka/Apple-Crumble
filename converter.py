### Converts .md lines into html
def convert_lines_to_html(contents : str, tag : str):
    if tag == "BR":
        return (f"<{tag}>")
    else:
        return (f"<{tag}> {contents} </{tag}>")

def convert_contents_to_html(contents : str): 
    words = contents.split()
    for i in range(len(words)):
        if words[i].startswith("**"):
            new_word = words[i].removeprefix("**")
            words[i] = "<strong>" + new_word
        elif words[i].startswith("*"):
            new_word = words[i].removeprefix("*")
            words[i] = "<em>" + new_word

        if words[i].endswith("**"):
            new_word = words[i].removesuffix("**")
            words[i] = new_word + "</strong>"
        elif words[i].endswith("*"):
            new_word = words[i].removesuffix("*")
            words[i] = new_word + "</em>"
    contents = " ".join(words)
    return contents