def pol(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    return pol(s[1:-1])

st = ' v b   nm  m  nb   V'
st = st.replace(' ', '')
st= st.lower()


print(pol(st))

    