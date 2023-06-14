
# folders = os.listdir("data")
# print(folders) #-> কি কি ফোল্ডার আছে সেইটা চেক করবে

# for folder in folders:
#     print(folder) #-> লিস্ট আকারে চেক করবে

# for folder in folders:
#      print(os.listdir(f"data/{folder}")) #-> ফোল্ডার এর মধ্যে কি কি ফাইল আছে সেইটা 											  রিড করবে

# for folder in folders:
#     print(folder) #-> ফোল্ডার প্রিন্ট করবে
#     print(os.listdir(f"data/{folder}")) #-> ফোল্ডার এর মধ্যে কি কি ফাইল আছে সেইটা 											রিড করবে

import os
# -> Check Directory

folder = os.listdir("data")
print(os.getcwd())
os.chdir("/programming")
print(os.getcwd())

# https://docs.python.org/3/library/os.html
# https://python.maateen.me/docs/os-module/