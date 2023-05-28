""" def welcome():
    print("Hello World")

print(__name__)
if __name__ == "__main__":
    welcome()
 """

""" 
    * __name__      :-  এই প্রগ্রামটা কোথা থেকে প্রিন্ট হবে (shanto.py)
    * "__main__"    :-  
 """

#  https://replit.com/@codewithharry/45-Day45-if-name-main-in-Python
# python book : 175


def welcome():
    print("Hello World Python")


print(__name__)
if __name__ == "__main__":
    welcome()
    print("Welcome Python")

# -> Problem IS
# -> shanto.py ফাইলের মধ্যে যদি আমরা ফাংশন ডিক্লিয়ার করি এবং সেই ফাংশন কল করি এবং import.py ফাইলের মধ্যে যদি shanto.py Module import করা হয় এবং কোড (import.py) রান করা হয় এর তাহলে "Hello World Python" ২ বার প্রিন্ট হয়। আমরা চাচ্ছি একবার প্রিন্ট হোক সেজন্য
""" 
-> if __name__ == "__main__": 
->  welcome() 
    
    * Module import করার ক্ষেত্রে অই মডিউলের if __name__ == "__main__"  অধিনে থাকা কোড রান হবেনা 
        *=> এর মানে shanto.py এর মধ্যে import.py এর if __name__ == "__main__" এই কন্ডিশনের মধ্যে যদি কোন কোড থাকে তাহলে সেইটা shanto.py এ রান করবে না। 
        
    * -> __name__ :-> এখানে এর মানে হচ্ছে, shanto.py হচ্ছে __main__ ফাইলে। 
    * -> এই main ফাইলের মধ্যে যেই ফাংশন কল করা হয়েছে সেইটা import ফাইলে প্রিন্ট করবে। 
    
"""
