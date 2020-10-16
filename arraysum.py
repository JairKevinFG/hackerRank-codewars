# 6
# 1 2 3 4 10 11 
# 31

n= int(input())
m = input().split()
m= list(map(int,m))
if len(m) == n:
    sumatotal = 0
    for i in m:
        sumatotal = sumatotal + i
    print(sumatotal)

