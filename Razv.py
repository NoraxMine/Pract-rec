st = '12345'

def razv(r):
    if len(r) == 1:
       return r
    return razv(r[1:]) + r[0]

print(razv(st))