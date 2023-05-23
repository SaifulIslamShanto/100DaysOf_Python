""" try:
    l = [1, 5, 6, 7]
    i = int(input("Enter The Index: "))
    print(l[i])
except:
    print("Some Error Occourred")

finally:
    print("I'm Always Executed")
 """
 
 
 
 
def func():
    try:
        l = [1, 5, 6, 7]
        i = int(input("Enter The Index: "))
        print(l[i])
        return 1
    except:
        print("Some Error Occourred")
        return 0

    finally:
        print("I'm Always Executed")

x = func();
print(x)

 
 
 
 
 
 
 
 
 


""" 
    * finally এইটা Execut হবেই
    * finally এইটা ফাংশন এর মধ্যে লেখে হইয়ে থাকে 
    
"""