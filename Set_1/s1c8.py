from binascii import a2b_hex

def detectECB(text):
    size = 16
    ts = set()
    for i in range(len(text)//16):
        ts.add(text[i*size : i*size+size])
    if(len(ts)!=len(text)//16):
        return True
    else:
        return False

if __name__ == "__main__":
    with open("s1c8.txt", 'r') as file:
        cnt=0
        for line in file:
            cnt += 1
            if detectECB(a2b_hex(line.strip())):
                print(a2b_hex(line.strip()), "line:", cnt)
            