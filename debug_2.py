n = 'AMD Athlon (34)'

s = ' '.join(n.split(' ')[:-1])


print(s, type(s))

s2 = ''
print(n[:n.index('(')] if '(' in n else n)