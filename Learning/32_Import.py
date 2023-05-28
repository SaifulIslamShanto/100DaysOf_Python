
# -> যে ফাংশন প্রয়োজন সেই শুধু ইম্পোর্ট করবে।
""" import math
result = math.sqrt(9)
print(result) """

# -> যে ফাংশন প্রয়োজন সেইটা শুধু ইম্পোর্ট করবে।
""" from math import sqrt, pi
result = sqrt(9)*pi
print(result) """

# -> যে ফাংশন প্রয়োজন সেইটার সব ডাটা ইম্পোর্ট করবে। => Not Recomended
""" from math import *
result = sqrt(9)*pi
print(result) """

# -> as কিওয়ার্ড ব্যবহার করে মডিউল / ফাংশন এর নাম ছোট বা মিনিংফুল করা যায়
""" from math import pi, sqrt as s
result = s(9)*pi
print(result) """
""" 
import math as math_builtin_pyhon
result = math_builtin_pyhon.sqrt(9)*math_builtin_pyhon.pi
print(result) """


# -> Dir Function
# -> এর মাধ্যমে একটি মডিউল এর মধ্যে কি কি ফাংশন বা ভেরিএব্ল আছে তা জানা যায় প্রিন্ট করে।


""" import math
print(dir(math))
print(dir(type(math)))
 """

# -> নিজের তেরি মডিউল ইম্পোর্ট করার নিয়মঃ

""" 
    * প্রথমে ফাইল hello.py খুলে হবে
    * এবার সেইটায় যে ফাংশন লেখার লিখতে হবে
    * এবার যাই ফাইলে ব্যবহার করবো use.py এ Import করতে হবে
    * from hello import welcome,harry
    * from hello import welcome(function),harry(variable)
    * from hello import * -> এতে করে hello.py এর সব কিছু এখানে চলে আসবে
"""

# from helloImport import welcome, shanto
# from helloImport import *
""" import helloImport as Hellos
Hellos.welcome()
print(Hellos.shanto) """


# -> Practice

# import tensorflow 
# print(dir(tensorflow))
