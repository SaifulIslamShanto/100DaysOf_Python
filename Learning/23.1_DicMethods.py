# Dictionary Methods in Python | Python Tutorial - Day #34
""" 
    * ডেটাবেজ এ বেশি কাজে লাগবে ডিকশনারি
    * https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
    * https://www.programiz.com/python-programming/dictionary
"""

epId = {122: 45, 123: 86, 567: 69, 670: 69}
epId2 = {222: 67, 566: 90}

# * epId.update(epId2) -> epId2 এর ভেলু epId তে চলে যাবে এবং আপডেট হইয়ে যাবে
# * epId.clear() -> epId তে যে ভেলু ছিলো তা মুছে যাবে।
# * epId.pop(122) -> সেলেক্টিভ ডাটা রিমোভ করে দেয়
# * epId.popitem() -> ডিকশনারি এর লাস্ট এর ডাটা রিমোভ করে দেয়
# * del epId -> ফুল ভেরিএব্ল রিমোভ করে দিবে
# * del epId[122] -> সেলেক্টিভ key রিমোভ করে দিবে

print(epId)

""" # -> খালি ডিকশোনারি এভাবে তেরি করতে হয়।
empt = {}
print(empt) """
