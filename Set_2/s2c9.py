def addpad(text, size):
    padlen = size - (len(text)%size)

    #print(padlen)
    
    if padlen==0:
        padlen = size
    text += bytes([padlen]) * padlen
    return text

def strippad(text):
    size = text[-1]
    return text[:-size]


if __name__ == "__main__":
    text =  b"YELLOW SUBMARINE"
    pdword = addpad(text, 32)
    print(pdword)
    sword = strippad(pdword)
    print(sword)
