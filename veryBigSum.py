n = int(input())
m = input().split()
m = list(map(int,m))
if n == len(m):
    sumatotal=0
    for i in m:
        sumatotal = i + sumatotal
print(sumatotal)