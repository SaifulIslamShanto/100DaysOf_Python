""" f = open("myFile.txt", 'r')
# ->  প্রথম লাইনে আমরা ফাইলটা রিড মোডে ওপেন করেছি
# print(f)
text = f.read() 
# -> দ্বিতীয় লাইনে ফাইলটা read() ফাংশনের (আসলে মেথড) সাহায্যে রিড করে ডাটা content ভ্যারিয়েবলে অ্যাসাইন করেছি।
print(text)
f.close()
#-> শেষ লাইনে close() ফাংশন (মেথড) ব্যবহার করে ফাইলটা ক্লোজ করে দিয়েছি।
 """

#  * Wriging A File

""" # f = open("myFile.txt", 'w') #*write
f = open("myFile.txt", 'a') #*append -> এক টেক্স বার বার এড হবে। 
f.write("Hello, World! Python")
f.close() """


""" f = open("myFile.txt", 'w') #*write
f.write("Hello, World! Python")
f.close()

with open("myFile.txt","a") as f:
    f.write(" Hello I'm Inside With") """

# -> open("FileName","Modes [r]")

""" my_file = open('myFile.txt','r')
content = my_file.read()
print(content)
my_file.close() """


# -> write("FileName","Modes [w]")

""" my_file = open('myFile.txt','w')
my_file.write("I am saiful islam shanto")
my_file.close() """

""" my_file = open('myFile.txt','a')
my_file.write(" , I am from Bangladesh.")
my_file.close() """

# ->

""" # *read() এর ভিতর আমরা 5 ভ্যালু পাস করেছি। এর ফলে ফাইলের প্রথম ৫ টা ক্যারেক্টার পর্যন্ত রিড হবে শুধু
my_file = open('myFile.txt', 'r')
content = my_file.read(5)
print(content)
# ****
content = my_file.read()
print(content)
# *tell() ফাংশন দিয়ে ফাইল পয়েন্টারের পজিশন খুঁজে বের করেছি
position = my_file.tell()
print(position)

# *seek() ফাংশন দিয়ে ফাইল পয়েন্টার আবার শুরুতে নিয়ে গিয়েছি
my_file.seek(8, 0)
content = my_file.read()
print(content)

my_file.close() """

# * ----------------------------------------

# my_file = open('myFile.txt', 'r')
""" with open('myFile.txt','r') as my_file:
    content = my_file.read()
    print(content) """


""" my_file = open('practice.txt', 'w')
for x in range(1, 101):
    print(x)
content = my_file.read()
my_file.close() """


with open('practice.txt', 'w') as file:
    for i in range(1, 101):
        file.write(str(i) + "\n")

x = open('practice.txt', 'r')
readFile = x.read()
print(readFile)
x.close()


""" এখানে কোডটির কাজ সম্পাদন হলেঃ

১. আমরা open() ফাংশন ব্যবহার করে "numbers.txt" নামের একটি ফাইল লিখতে "w" মোডে ওপেন করি। ফাইলটি যদি অস্তিত্ব না থাকে, তবে নতুনভাবে তৈরি করা হবে এবং যদি অস্তিত্ব থাকে, তবে আগের সকল উপাদানগুলি মুছে ফেলা হবে।

২. আমরা for লুপ ব্যবহার করে range() ফাংশনের মাধ্যমে ১ থেকে ১০০ পর্যন্ত সংখ্যাগুলির উপর পরিবর্তনশীল হবার জন্য লুপ চালাই।

৩. লুপের ভিতরে, আমরা str(i) ব্যবহার করে প্রতিটি সংখ্যাকে স্ট্রিং ট্রান্সফরম করে নেই এবং এরপরে এটির সাথে একটি নতুন লাইন চিহ্ন "\n" যুক্ত করি। এটি নিশ্চিত করে যে প্রতিটি সংখ্যা টেক্সট ফাইলে নতুন লাইনে লিখতে হবে।

৪. আমরা ফাইল অবজেক্টের write() মেথডের মাধ্যমে সংখ্যার স্ট্রিং প্রতিস্থান লিখে ফাইলে লিখছি।

৫. শেষমেশ, লুপটি শেষ হওয়ার পরে, আমরা ফাইলটি বন্ধ করছি। এটি with স্টেটমেন্ট ব্যবহার করে করা হয়, যা নিশ্চিত করে দেয় যে যদি একটি ব্যতিক্রম ঘটতে পারে তবে ফাইলটি সঠিকভাবে বন্ধ করা হয়ে যাবে।

এই কোডটি চালানোর পরে, আপনি আপনার পাইথন স্ক্রিপ্টের সমান ডিরেক্টরিতে "numbers.txt" নামের একটি ফাইল পাবেন, যা পুনরায় পাইথন স্ক্রিপ্টের কাছে থাকবে এবং একটি নতুন লাইনে প্রতিটি সংখ্যা সহ, ১ থেকে ১০০ পর্যন্তের সংখ্যা সম্মিলিত থাকবে। """
