n = input()
t = int(input())
i=0 

while i < len(n):
    print(n[i:i+t])
    i = i + t 

import textwrap
s = input()
w = int(input())
print(textwrap.fill(s,w))