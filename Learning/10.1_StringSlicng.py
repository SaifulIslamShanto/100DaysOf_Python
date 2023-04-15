""" name = "Shanto"
print("Length Of the Word : ",len(name))
print(name[0:6]) """

fruit = "mango"
len1 = len(fruit)
print(len1)
# print(fruit[0:4]) #including 0 but not 4
# print(fruit[:4]) #automaticaly Add 0 #including 0 but not 4
# print(fruit[1:4]) #including 1 but not 4
# print(fruit[1:]) #add length  #including 1 & Length
# print(fruit[0:-3]) #print(fruit[0:len(fruit = 5)-3])
# print(fruit[-1:-3]) #print(len(fruit = 4)fruit[-1:len(fruit = 5)-3])
print(fruit[-3:-1]) #print(len(fruit = 4)fruit[-1:len(fruit = 5)-3])
print("Mango is a", len1, "Letter word.")


""" nm="Harry"
print(nm[-4:-2]) 
# -> len 5 - 4 -> 1 : len 5 - 2 -> 3 
# -> print 1:3
print(nm[-5:-1]) 
print(nm[0:4]) 
# -> len 5 - 5 -> 0 : len 5 - 1 -> 4 
# -> print 0:4 => Har """