# numero complejo => z=x+yi
# r = suma de cuadrados = abs(complex(-1.0,0.0))
# angulo de fase (argumento) =  phase(complex(-1.0,0.0))
# coordenada polar =>  modulo r y el angulo de fase 
import cmath


complejo = input()

print(abs(complex(complejo)))
print(cmath.phase(complex(complejo)))


