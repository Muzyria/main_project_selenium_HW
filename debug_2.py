import re

n = ['Intel Core i9 (13)\nIntel Core i7 (20)\nIntel Core i5 (34)\nIntel Core i3 (12)\nIntel Pentium (7)\nIntel Celeron (6)\nAMD Ryzen Threadripper (2)\nAMD Ryzen 9 (6)\nAMD Ryzen 7 (14)\nAMD Ryzen 5 (23)\nAMD Ryzen 3 (8)\nAMD A12 (2)\nAMD A10 (1)\nAMD A8 (1)\nAMD A6 (2)\nAMD Athlon (5)']

s = list(map(str, n[0].split('\n')))
print(s)

for item in s:
    # r = ''.join(re.findall(r'(\s\(\d\))', item))
    # print(r)
    # item.replace(r, '')
    print(' '.join(item.split(' ')[:-1]))