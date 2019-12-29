a = input('word: ')
b = input('word2: ')
v = set(a)
n = set(b)
if v.intersection(n):
    print('Yes')
else:
    print('No')
