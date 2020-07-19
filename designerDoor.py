n,m = map(int,input().split())

v1 = '-'
v2 = '.|.'
v3 = "WELCOME"

for i in range(n//2):
    print((v2*((2*i)+1)).center(m,v1))

print(v3.center(m,v1))

for i in range(n//2,0, -1):
    print((v2*((2*i)-1)).center(m,v1))
    