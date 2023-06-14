# 'is' vs '==' in Python | Python Tutorial - Day #54

""" 
    * a Comparison Operator
        * is ->  exact location of object in memory
             -> is এর দিয়ে Comparison করলে সে চেক করে তার মেমোরি এড্রেস সেম কিনা । যদি সেম হয় তাহলে True রিটার্ন করে অন্যথায় False রিটার্ন করে 
             -> id(var_Name)  দিয়ে মেমোরি লোকেশন চেক করা যায়
        * == ->  value
"""

# a = 4  # -> 140703666660232
# b = '4'  # -> 140703666703656
a = [4, 5, 6] #-> 2295398355776
b = [4, 5, 6] #-> 2295399823424
# a = (4, 5, 6) #-> 2352065667520
# b = (4, 5, 6) #-> 2352065667520
# a = None
# b = None
print(id(a))
print(id(b))
print(a is b)
print(a == b)

# https://towardsdatascience.com/whats-the-difference-between-is-and-in-python-dc26406c85ad
#
