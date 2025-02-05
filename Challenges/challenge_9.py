def cleanup(text:str) -> str:
    for char in "!","?",".":
        text = text.replace(char,"")
    text = text.strip()
    text = text.lower()
    return text
print(cleanup("  Hello!  "))