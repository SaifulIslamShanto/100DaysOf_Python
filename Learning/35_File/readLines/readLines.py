# Read Line by Line Code
# -> readLine ব্যভাহার করে যতক্ষন

f = open('readLine.txt', 'r')
i = 0

while True:
    i = i+1
    line = f.readline()
    if not line:
        # print(line, type(line))
        break
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])
    print(f"Marks of studnets {i} in maths is : {m1*2} ")
    print(f"Marks of studnets {i} in English is : {m2*2} ")
    print(f"Marks of studnets {i} in Bangla is : {m3*2} ")

    print(line)
