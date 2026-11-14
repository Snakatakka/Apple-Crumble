### Converts .md lines into html
def convert_lines_to_html(contents : str, tag : str):
    if tag == "br":
        return (f"<{tag}>")
    else:
        return (f"<{tag}> {contents} </{tag}>")

def convert_contents_to_html(contents : str): 
    words = contents.split()
    
    for i in range(len(words)): # This is so fucked dude
        words[i] = get_bold_and_italic(words[i])
    
    contents = " ".join(words)
    return contents

def get_bold_and_italic(word : str):
    if word.startswith("***") or word.startswith("___"):
        new_word = word.removeprefix("***").removeprefix("___")
        word = "<strong><em>" + new_word
    elif word.startswith("**") or word.startswith("__"):
        new_word = word.removeprefix("**").removeprefix("__")
        word = "<strong>" + new_word
    elif word.startswith("*"):
        new_word = word.removeprefix("*").removeprefix("_")
        word = "<em>" + new_word

    if word.endswith("***") or word.endswith("___"):
        new_word = word.removesuffix("***").removesuffix("___")
        word =  new_word + "</em></strong>"
    elif word.endswith("**"):
        new_word = word.removesuffix("**").removesuffix("__")
        word = new_word + "</strong>"
    elif word.endswith("*"):
        new_word = word.removesuffix("*").removesuffix("_")
        word = new_word + "</em>"
    
    return word