def step(x, n):
    if n==0:
        return 1
    return step(x, n-1)*x

f = step(2,10)
print(f)