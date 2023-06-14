# Lambda functions in Python | Python Tutorial - Day #52
# * এই ফাংশন ব্যবহার করে ফাংশন কে সহজে ১ লাইনের মধ্যে লেখা যায়
""" 
    * সাধারণভাবে যখন def কিওয়ার্ড ব্যবহার করে একটি ফাংশন তৈরি করা হয় তখন স্বয়ংক্রিয় ভাবে এটিকে একটি ভ্যারিয়েবলে অ্যাসাইন করে দেয়া হয় যার মাধ্যমে একে পরবর্তীতে কল করা যায়
"""

# def double(x):
#     return x*2


# def double(x): return x*2
# * lambda arguments : expression

def apply(fx,value):
    return 6+fx(value)

double  = lambda x: x*2
cube = lambda x: x*x*x
avg = lambda x,y,z:(x+y+z)/3

print(double(5))
print(cube(5))
print(avg(3,5,10))

print(apply(cube, 2))
# print(apply(lambda x: x*x*x, 2))
