def dig(s):
    if len(s) == 0:
        return 0 
    return s[0] + dig(s[1:])
a = dig([3,3,4,2,7])
print(a)
