""" with open('35_file/seek.txt', 'r') as f:
    print(type(f))

    # Move to the 10th bytes in the file
    f.seek(10)

    # read the next 5 bytes
    data = f.read()
    print(data)
 """
datas = open('35_file/seek.txt', 'r')
content = datas.read()
print("Full TEXT : ", content)

# -> MOve to the 10th Bytes in the files
content = datas.seek(10)

print("Skip Data : ",datas.tell())
# -> Read The Next 5 Bytes
content = datas.read(5)
print("after skip TEXT ; ", content)
