import math

a = int(input())
b = int(input())

resultado = math.atan(a/b)
grados = resultado*180/math.pi
if grados-int(grados) >= 0.5:
    print(f'{int(grados+1)}°')
else:
    print(f'{int(grados)}°')
    
