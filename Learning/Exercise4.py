

str = input("Enter Message : ")
words = str.split(" ")
coding = True
if (coding):
    for word in words:
        nwords = []
        if (len(str) >= 3):
            rendom1 = "xyz"
            rendom2 = "CSK"
            strNew = rendom1 + word[1:] + word[0] + rendom2
            nwords.append(strNew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))  # *ello PythonH

else:
    pass

""" 
* SKIP 
* Exercise 4: Solutions and Shoutouts | Python Tutorial - Day #47
 """