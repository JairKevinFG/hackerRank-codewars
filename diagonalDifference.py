#diagonal difference 
# 3
# 11 2 4
# 4 5 6
# 10 8 -12
# salida : 15
primary_diagonal = 0
secondary_diagonal = 0
matriz=[]
n = int(input())
i =0 
while(i<n):
    i=i+1
    x=input().split()
    x = list(map(int,x))
    matriz.append(x)
for i in range(0,len(matriz)):
    primary_diagonal = matriz[i][i] + primary_diagonal
    secondary_diagonal = matriz[i][len(matriz)-i-1]+ secondary_diagonal
difference_abs = abs(primary_diagonal - secondary_diagonal)
print(f'{difference_abs}')


