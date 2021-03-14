import binascii

sa = "1c0111001f010100061a024b53535009181c"
sb = "686974207468652062756c6c277320657965"
d = "746865206b696420646f6e277420706c6179"

ba = binascii.a2b_hex(sa)
bb = binascii.a2b_hex(sb)


ans = bytes(a^b for a,b in zip(ba, bb)).hex()
print(d, ans, d==ans, sep="\n")
