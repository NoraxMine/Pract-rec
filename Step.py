def step(x, n):
    if n==0:
        return 1
    return step(x, n-1)*x

v = input()
y,k = v.split()
y = int(y)
k = int(k)

f = step(y,k)
print(f)