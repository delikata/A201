def is_anagram(str1,str2):
    count=0
    if(len(str1)!=len(str2)):
        return False
    i=0
    while(i<len(str1)):
        j=0
        while(j<len(str2)):
            if(str1[i]==str2[j]):
                count=count+1
                str2.remove(str2[j])
            j=j+1
        i=i+1
        
    if(count==len(str1)):
        return True
    else:
        return False
str1=raw_input("Enter your first String: ")
str2=raw_input("Enter your Second String: ")
str1=list(str1)
str2=list(str2)
print is_anagram(str1,str2)
