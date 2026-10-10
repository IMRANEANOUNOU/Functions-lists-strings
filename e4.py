def Occur(text,lettre):
    n=0
    for l in list(text) :
        if l==lettre : n+=1
    return n

st = ""

print(Occur(st,"a"))



#Q-2
def O(t, l):
    if t == "":
        return 0

    if t[0] == l:
        return 1 + O(t[1:], l)
    else:
        return O(t[1:], l)
stri = "aabbcda"
print(O(stri,"a"))
