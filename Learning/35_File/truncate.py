with open('35_File/truncate.txt', 'w') as f:
    f.write("Hello World!_xyz ")
    f.truncate(3)

with open('35_File/truncate.txt', 'r') as f:
    print(f.read())
