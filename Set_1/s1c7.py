from Crypto.Cipher import AES
from base64 import b64decode, b64encode

if __name__ == "__main__":
    key = b"YELLOW SUBMARINE"
    cipher = AES.new(key, AES.MODE_ECB)
    with open("s1c7.txt", "rb") as file:
        word = file.read()
    cipherBytes = b64decode(word)
    ans = cipher.decrypt(cipherBytes)
    print(ans.decode('utf-8'))