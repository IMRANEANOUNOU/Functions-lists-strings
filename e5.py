
def palindrome(mot):
    if len(mot) <= 1:
        return True

    if mot[0] != mot[-1]:
        return False

    return palindrome(mot[1:-1])


mot = input("donner un mot : ")

if palindrome(mot):
    print("un palindrome")
else:
    print("pas un palindrome")
