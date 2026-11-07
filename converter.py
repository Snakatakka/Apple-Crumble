### Converts .md lines into html
def convert_to_html(contents : str, tag : str):
    if tag == "BR":
        return (f"<{tag}>")
    else:
        return (f"<{tag}> {contents} </{tag}>")