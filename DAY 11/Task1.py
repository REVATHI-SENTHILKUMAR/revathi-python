#Remove Duplicate Characters from a String 


def remove_duplicate_chars(s):
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return "".join(result)

print(remove_duplicate_chars("programming")) 
