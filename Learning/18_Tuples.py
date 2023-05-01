""" 
    -> Tuple এর ভেলু চেঞ্জ করা যায়না
    -> যদি একটি সংখ্যা বা লেখা হয় তাহলে (,) কমা দিতে হবে নাহ্লে int ডেটা টাইপ দেখাবে
        *   tup = (1,)
        *   print(type(tup),tup)
    => https://replit.com/@SaifulIslamShan/24-Day24-Introduction-to-Tuples
"""

""" tup = (1, 5, 6, "Shanto" , True)
print(type(tup), tup)
print(type(len), tup)
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[4])

tup2 = (tup[1:4])
print(tup2) """

""" tuple1 = (1,2,2,3,5,4,6)
tuple2 = ("Red", "Green", "Blue")
print(tuple1)
print(tuple2)

details = ("Abhijeet", 18, "FYBScIT", 9.8)
print(details)


country = ("Spain", "Italy", "India", "England", "Germany")
#            [0]      [1]      [2]       [3]        [4]
print(country[-1]) # Similar to print(country[len(country) - 1])
print(country[-3])
print(country[-4]) """


""" country = ("Spain", "Italy", "India", "England", "Germany")
if "Italy" in country:
    print("Italy is present.")
else:
    print("Italy is absent.") """

animals = ("cat", "dog", "bat", "mouse",
           "pig", "horse", "donkey", "goat", "cow")
print(animals[3:7])  # using positive indexes
print(animals[-7:-2])  # using negative indexes'
