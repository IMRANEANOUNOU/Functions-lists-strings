def grands(L,x):
    s = 0
    for i in range(len(L)):
        if L[i]>x:
            s=s+1
    return s


t = grands([1,2,3,4],4)
print(t)

#complexite est O(n) :
# s=0 , affectation O(1)
# for .. c'est une boucle donc c'est : O(n)
# if , condition O(1)
# s= s+1 , O(1)
# ...
# print(x) , O(1)
# 
# D'ou C = O(1) + O(n) = O(n)

def petits(L,x):
    n = 0
    for i in range(len(L)):
        if L[i]<x  : n+=1
    return n


v = petits([1,2,3,4],4)
print(v)


def median(L):
    n = len(L)
    for i in range(n):
        if grands(L,L[i]) <= n/2 and petits(L,L[i]) <= n/2:
            return L[i]
    
    
        
S = [25 , 12 , 6 , 17, 3 , 10 , 20 , 12 , 15 ,
38]

print(median(S))
