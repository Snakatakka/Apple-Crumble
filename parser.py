def parse_tag(line : str): # This code sucks but Python doesn't have switch cases so this is how im doing it
    if line == "\n":
        return "BR"
    elif line.startswith("#"):
        number_of_hashes = 0
        increment = 0

        while True:
            if line[increment] == "#":
                number_of_hashes += 1
                increment += 1
            else:
                if number_of_hashes > 6: # Limits heading to H6 since thats the smallest a heading can go
                    number_of_hashes = 6 
                break

        return ("H" + str(number_of_hashes))
    else:
        return "P"

def parse_contents(line : str, tag : str):
    tags = { # There's most definitely a better way to do this but im lazy.
        'H1' : '# ', # The extra space is intentional so that the contents don't all begin with a space
        'H2' : '## ',
        'H3' : '### ',
        'H4' : '#### ',
        'H5' : '##### ',
        'H6' : '###### ',
        'P' : '' # The paragraph doesn't have a space because it doesn't have a prefix
    }

    if tag == 'BR':
        return '\n'
    else:
        return line.strip(tags[tag]).strip("\n") # Returns the stuff in the line without the tags at the beginning.