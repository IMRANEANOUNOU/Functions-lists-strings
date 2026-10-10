s1 = "abc"
s2="de"

res = []
for i in s1:
     for j in s2:
         res.append(i+j)
print(list(res))

#version demander dans la question 2 est comme cela :

result = map(lambda x : x[0]+x[1] , [(i,j) for i in s1 for j in s2] )

print(list(result))
