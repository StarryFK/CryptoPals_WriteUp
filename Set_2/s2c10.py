from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from base64 import b64decode

def bytesXorBytes(bt1, bt2):
    bt2 = bt2 * (len(bt1)//len(bt2) + 1)
    return bytes([a^b for a,b in zip(bt1, bt2)])

def AES_CBC_encrypt(btext, key, iv, size):
    if len(btext)%size !=0:
        rest = size - (len(btext) % size)
    else:
        rest = size   
    btext += bytes([rest]) * rest
    cipher = AES.new(key, AES.MODE_ECB)
    etext = cipher.encrypt(
        bytesXorBytes(
            btext[0:size], iv))
    for i in range(1,len(btext)//size):
        etext += cipher.encrypt(
            bytesXorBytes(
                btext[i*size:i*size+size], 
                etext[(i-1)*size:i*size]))    
    return etext
    
def AES_CBC_decrypt(etext, key, iv, size):
    cipher = AES.new(key, AES.MODE_ECB)
    btext = bytesXorBytes(
        cipher.decrypt(etext[0:size]),
        iv
    )
    for i in range(1, len(etext)//size):
        btext += bytesXorBytes(
            cipher.decrypt(etext[i*size:(i+1)*size]),
            etext[(i-1)*size:i*size]
        )
    btext = btext[0:-btext[-1]]
    return btext

if __name__ == "__main__":
    with open("s2c10.txt", "r") as file:
        etext = b64decode(file.read())
    key = b"YELLOW SUBMARINE"
    iv = b"\x00"
    btext = AES_CBC_decrypt(etext, key, iv, 16)
    print(btext.decode("ascii"))

    cipher = AES.new(key, AES.MODE_CBC, iv*16)
    print(unpad(cipher.decrypt(etext), 16).decode('ascii'))