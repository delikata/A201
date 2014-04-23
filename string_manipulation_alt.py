def space_letters(incoming):
    newstring=""
    for i in incoming:
        newstring=newstring +i+" "
    return newstring
def space_letters_alt(incoming):
    i = len(incoming)
    j=0
    newstring=""
    while j<i:
        newstring=newstring +incoming[j:j+1]+" "
        j = j +1
    return newstring
def reverse_string(incoming):
    j = len(incoming)
    newstring= ""
    while j > -1:
        newstring = newstring + incoming[j:j+1]
        j = j-1
    return newstring


print (space_letters_alt('For British Eyes Only'))
print (space_letters("Hello"))
print (reverse_string("How are you"))
