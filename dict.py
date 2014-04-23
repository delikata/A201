D = {}
word = ""
while word != "q":
    word = input ("Input a word to define or see the definition of: ")
    if word in D:
        print (D[word])
    elif word == "q":
        print ("Thank you goodbye")
    else:   
        D[word] = input ("what is the definition of " + word + " ")
