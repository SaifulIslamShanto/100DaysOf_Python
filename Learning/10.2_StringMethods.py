# String Mythod
# immutable  -> Can't Change | String are immutable
a = "shoantooo"
b = "shanto !!!!"
print(len(a))
print(a.upper())  # -> Convert in uppercase
print(a.lower())  # -> Convert in loercase
print(a.rstrip("!"))    # -> shanto !!!! to shanto [Remove !]
print(a.replace("shanto", "Saiful"))  # -> replace string -> Saiful
print(b.split(" "))  # -> ['shanto', '!!!!']
blogHeading = "introducing to python"
print(blogHeading.capitalize())
print(blogHeading.center(50))  # -> Add spaces and make it center

#------------------------------------------------

#-> এখানে চেক করবে word এর মধ্যে কয়টা "o" বা "Sentence" আছে সেগুলো গুনে।  
print(a.count("o"))  # count the word OR sentes

#------------------------------------------------

#-> এখানে চেক করবে last word endswith এ আছে কিনা। যদি থাকে ত হলে বুলিয়ান ভেলু শো করবে।
str1 = "Welcome to console !!!"
print(str1.endswith("!!!"))
print(str1.endswith("to", 4, 10))

#------------------------------------------------

#-> এখানে প্রথম is যেখানে আছে সেখানে কার ইন্ডেক্স Show করবে  => 10
str2 = "he's name is DAN. He is and honest man."
print(str2.find("is"))
print(str2.index("is"))

#------------------------------------------------

#-> 

str3 = "WelcomeToTheConsole"
print(str3.isalnum()) #true

# str4 = "Welcome" #true
str4 = "Welcome00" #False
print(str4.isalpha())


str5 = "hello world python" #true
str5 = "hello world Python" #False
print(str5.islower()) 

#-> isprintable() => True / False

str5 = "we wish to get job in google"#true
str5 = "we wish to get job in google\n"#False
print(str5.isprintable())


#-> isspace() => True / False
str6 = "        " #using Spacebar
str7 = "        " #using Tab
print(str6.isspace())#true
print(str7.isspace())#true


str8 = "Python Is Good For Learning Programming" #true
str8 = "Python is Good For Learning Programming" #False
print(str8.istitle())


str9 = "Hello World"#true
str9 = "Hello world"#False
print(str9.istitle())


str10 = "hello world"
str10 = "HELLO WORLD"
print(str10.swapcase())









# mutable    -> An object whose internal state can be changed is mutable
# immutable  -> Can't Change
