def func(n):
    l = [i for i in range(n+1)]
    res = map(lambda x : x+3,l)
    return res

print(list(func(3)))
