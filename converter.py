### Converts .md lines into html
def convert_lines_to_html(contents : str, tag : str):
    if tag == "br":
        return (f"<{tag}>")
    else:
        return (f"<{tag}> {contents} </{tag}>")

def convert_contents_to_html(contents : str): 
    words = contents.split()
    
    for i in range(len(words)):
        if words[i].startswith("***") or words[i].startswith("___"):
            new_word = words[i].removeprefix("***").removeprefix("___")
            words[i] = "<strong><em>" + new_word
        elif words[i].startswith("**") or words[i].startswith("__"):
            new_word = words[i].removeprefix("**").removeprefix("__")
            words[i] = "<strong>" + new_word
        elif words[i].startswith("*"):
            new_word = words[i].removeprefix("*").removeprefix("_")
            words[i] = "<em>" + new_word

        if words[i].endswith("***") or words[i].endswith("___"):
            new_word = words[i].removeprefix("***").removeprefix("___")
            words[i] =  new_word + "</em></strong>"
        elif words[i].endswith("**"):
            new_word = words[i].removesuffix("**").removesuffix("__")
            words[i] = new_word + "</strong>"
        elif words[i].endswith("*"):
            new_word = words[i].removesuffix("*").removesuffix("_")
            words[i] = new_word + "</em>"
    
    contents = " ".join(words)
    return contents