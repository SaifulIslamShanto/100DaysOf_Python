""" class person:
    name = "Dhanto"
    occ = "Developer"

    def info(self):
        print(f"{self.name} is a {self.occ}")


a = person()
print(a.name)
print(a.occ)
a.info() """

# **********************************


""" class person:
    def __init__(self, name, occ):
        self.name = name
        self.occ = occ

    def info(self):
        print(f"{self.name} is a {self.occ}")


a = person("Shanto", "Developer")
a.info()
 """


class Monster:
    def __init__(self, color, heads):
        self.color = color
        self.heads = heads

    def attack(self):
        print("Just attacked a Hero, Mu...hahahaha!!!")

# Create an instance/object/monster-character
mournsnake = Monster("Yellow", 4)
# Check if its created or not
print('I am a ' + str(mournsnake.heads) + ' headed monster.')
# Make an attack by the new monster
mournsnake.attack()



# * https://python.howtocode.dev/oop-python/class

""" 
 ->     যদি আমরা ক্লাসের ভিতর কোন ভ্যালু পাস করতে চাই? আর পরে যদি সেই ভ্যালু নিয়েই মেথডের ভিতর কোডিং কারিশমা ফলাতে চাই? তখন ক্লাসের প্রথম মেথড হিসাবে __init__ ব্যবহার করতে হবে। প্রোগ্রামিংয়ের ভাষায় একে ক্লাস কনস্ট্রাক্টর (constructor) বলে।
 ->     যখন কোন ক্লাসের নতুন ইন্সট্যান্স বা অবজেক্ট তৈরি করি আমরা তখন পাইথন নিজ থেকেই ক্লাস কনস্ট্রাক্টরকে কল করে। 

"""