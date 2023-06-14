
with open("PracticeProgram/File_Program/01_ReadFromTextFile/read.txt", 'r') as f:
    # lines = f.readlines()
    lines = f.read().split("\n\n\n\n")
    print(lines)
