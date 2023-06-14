# Find the Factorial of a Number

""" 
-> ফ্যাক্টরিয়াল একটি গণিতিক পরিসংখ্যান অপারেশন যা একটি ধনাত্মক পূর্ণসংখ্যার (সাধারণত n নামে পরিচিত) জন্য ব্যবহার করা হয়। ফ্যাক্টরিয়াল নং নিয়ে তার সমস্ত পূর্ণসংখ্যার (শূন্য সহ) গুনফল নিয়ে একটি মান উপস্থাপন করে।

n এর জন্য ফ্যাক্টরিয়াল সমান হবে:

n! = n × (n - 1) × (n - 2) × ... × 3 × 2 × 1

যেমনঃ
5! = 5 × 4 × 3 × 2 × 1 = 120

ফ্যাক্টরিয়াল সংখ্যা পূর্ণসংখ্যা হয় এবং সমান্তরাল ব্যবহার করে প্রকাশ করা হয়, যাতে অঙ্কের মাঝে কোনো অক্ষর থাকে না। ফ্যাক্টরিয়াল অপারেশনের ব্যবহার প্রতিষ্ঠান গণিতে, কম্পিউটার বিজ্ঞানে, ফিজিক্সে, সংখ্যাতত্ত্বে এবং অন্যান্য বিজ্ঞান শাখাগুলিতে দেখা যায়। """

# Socilation - 1

""" num = int(input("Enter a Number : "))
fact = 1

if (num < 0):
    print("Factorial of 0 Does not Exist")
elif (num == 0):
    print("Factorial of 0 is", 1)
elif (num > 0):
    for i in range(1, num+1):
        fact = fact*i

print("The Facetorial of the given Number is :", fact) """


# Socilation - 2

def facet(a):
    if (a == 0):
        return 1
    else:
        return (a)*facet(a-1)


num = int(input("Enter a Number here : "))
result = facet(num)
print("The Facetorial of the given Number is :", result)
