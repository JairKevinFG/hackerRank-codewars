# 5 6 7
# 3 6 10
# salida : 1 1
m = input().split()
n = input().split()
m = list(map(int,m))
n = list(map(int,n))
m_puntos = 0
n_puntos = 0
for i in range (0,len(m)):
    if m[i] > n[i]:
        m_puntos = m_puntos + 1
    elif m[i] < n[i]:
        n_puntos = n_puntos + 1 

print(f'{m_puntos} {n_puntos}')