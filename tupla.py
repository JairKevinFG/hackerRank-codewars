n = int(input())
lines = input().split()
elements = list(map(int,lines))
if n == len(elements):
    tupla = tuple(elements)
    print(hash(tupla))
