a = 10
print(type(a))
b = "shanto"
print(type(b))
c = True
print(type(c))
d = None
print(type(d))
e = 10.1
print(type(e))
f = complex(10.1)
print(type(f))
list1 = [8, 2, 3, [-4, 5], ["apple", "android"]]
print(list1)


'''
    => Datatype
        * builtin Data Type
            ->> numbar 
                -> int 
                -> float 
                -> complex || f = complex(10.1)
                
            ->> String text data
                -> str:"hello world"
                
            ->> Boolean data:
                -> True
                -> False
            
            ->> sequenced data : list, tuple
                -> list
                    =>> Collection of diffrent type of data
                    --> list1 = [8,2,3,[-4,5],["apple","android"]]
                    --> print(list1)
                --> tuple
                    ==> mutation --> changes
                    ==> imutation --> don't chanagble 
                        -> tuple is immutable
                        -> tuple1 = (("parrot","sparrow"),("lion","Tiger"))
                        -> print(tuple1)
                        
            ->> mapped data: dict
                -> we can store data using keyword
                -> dict1 = {"name":"shanto", "age":20, "canVote":True}
                -> print(dict1);
                
            ==> everyting is object in python
            
'''
