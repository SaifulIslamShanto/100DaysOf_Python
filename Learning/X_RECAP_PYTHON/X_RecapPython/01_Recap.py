# Function

""" def sum(x, y):
    return x+y


print(sum(10, 20)) """

# person_name = "Santo"
# print(len(person_name))

# -> List
""" gerocery_list = ["rice", "Potato", "Tomato"]
print(gerocery_list)
gerocery_list.append("Banana") #-> Append Object Method
print(gerocery_list) """


""" l2 = list()
l2.append(2)
print(l2) """


""" gerocery_list = ["rice", "Potato", "Tomato"]
print(gerocery_list[2])
print(gerocery_list[-3]) """

# -1 => 2[Tomato]
# -2 => 1[Potato]
# -3 => 0[rice]

""" gerocery_list = ["rice", "Potato", "Tomato"]
print(gerocery_list)
gerocery_list.sort()
print(gerocery_list) """

""" number = [1, 2, 4, 7, 86, 5, 8, 7, 49, 8, 74, 45]
sorted_List = sorted(number)
print(number)
print(sorted_List)
 """

#  -> Loops


""" def is_even(number):
    if (number % 2 == 0):
        return True
    else:
        return False


startring = 0
even_number = []
user_input = int(input("Limits : ")) """

""" while startring <= user_input:
    if is_even(startring):
        even_number.append(startring)

    startring = startring+1

print(f"Even Numbers : {even_number}")
print("Finished") """

""" startring = 0
while startring < 100:
    if is_even(startring):
        print(f"{startring} is Even")
    else:
        print(f"{startring} Is Odd")
        
    startring = startring+1

print("Finished") """

""" for num in range(0, user_input+1):
    if is_even(num):
        even_number.append(num)


print(f"Even Numbers : {even_number}")
print("Finished") """


# grocery = ["rice", "Potato", "Tomato", "tomato"]

""" for item in grocery:
    if item == 'water':
        continue
    print(item) """

# for i in range(0, 10, 2):
""" for i in range(0, len(grocery)):
    print(grocery[i])
 """

# -> FILE IO


""" with open('Learning/X_RecapPython/textFile.txt', 'r') as s_file:
    words_all = []
    # unique_word = set()
    for line in s_file.readlines():
        # print(line, end="")
        # print(line.strip(), end="")
        # print(line.strip())
        # stripped_String = line.strip()
        word = line.strip().split(" ")
        words_all += word

    unique_word = set(words_all)
    # print(len(words_all))
    print(len(words_all))
    print(len(unique_word))

    with open('Learning/X_RecapPython/unique_words.txt', 'w') as write_file:
        for item in sorted(unique_word):
            write_file.write(item)
            write_file.write(" \n")

print("Finshed") """


userName = input("Your Name : ")
value = 1
newString = value+userName

print(newString)