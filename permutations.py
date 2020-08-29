from itertools import permutations

m,n = input().split()
string= ""

lista = []
newlist = list(permutations(m,int(n)))

for i in newlist:
    for j in list(i):
        string = string + j
    lista.append(string)
    string=""   

for i in sorted(lista):
    print(i)


# AC
# AH
# AK 
# CA 
# CH 
# CK 
