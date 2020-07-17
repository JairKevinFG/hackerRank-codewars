def mutate_string(s,i,c):
    lista = list(s)
    lista[i] = c
    string = ''.join(lista)
    return string

def run():
    s = input()
    i , c = input().split()
    s_new = mutate_string(s,int(i),c)
    print(s_new)

run()
