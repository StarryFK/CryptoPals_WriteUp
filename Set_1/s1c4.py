from s1c3 import decode3, score

with open("s1c4.txt", "r") as f:
    arr = []
    for line in f:
        line = line.strip()
        arr.append(decode3(line))

    arr.sort(key=lambda x:x[2], reverse=True)
    for i in range(5):
        print(arr[i])