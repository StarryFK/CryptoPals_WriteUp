import base64

def bytesXorBytes(bytes1, bytes2):
    z = zip(bytes1, bytes2)
    return bytes(a^b for a,b in z)

def hammingDistance(bytes1, bytes2):
    bxor = bytesXorBytes(bytes1, bytes2)
    return sum(bin(b).count('1') for b in bxor)

def guessKeySize(cipherString):
    can = []
    for KEYSIZE in range(1,50):
        arr = []
        for i in range(20):
            sc1 = slice(i*KEYSIZE, i*KEYSIZE+KEYSIZE)
            sc2 = slice(i*KEYSIZE+KEYSIZE, i*KEYSIZE+2*KEYSIZE)
            arr.append(hammingDistance(cipherString[sc1], cipherString[sc2])/KEYSIZE)
        ans = sum(arr)/len(arr)
        can.append((KEYSIZE, ans))
    can.sort(key=lambda x:x[1])
    return can[0][0]

def guessStringXorChar(bytestring):
    engword = ({a for a in range(ord('a'), ord('z'))} 
               | {a for a in range(ord('A'), ord('Z'))} 
               | {ord(' ')})
    can = []
    for ch in range(0, 256):
        s = [ch^i for i in bytestring]
        score = 0
        for i in s:
            if i in engword:
                score += 1
        can.append((ch, score))
    can.sort(key=lambda x:x[1], reverse=True)
    return can[0][0]

def cipherXorKey(cipherText, Key):
    keystream = Key*(len(cipherText)//len(Key) + 1)
    return bytesXorBytes(keystream, cipherText)


if __name__ == '__main__':
    with open("s1c6.txt", 'r') as file:
        cipherString = base64.b64decode(file.read())
        KEYSIZE = guessKeySize(cipherString)
        keylist = []
        for i in range(KEYSIZE):
            sc = slice(i, i+30*KEYSIZE, KEYSIZE) 
            ch = guessStringXorChar(cipherString[sc])
            keylist.append(chr(ch))
        key = ''.join(keylist)
        ans = cipherXorKey(cipherString, key.encode()).decode('ascii')
        print("Key: %s\nText:\n%s\n" % (key, ans))
        