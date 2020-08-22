# tengo una lista con letras , eliminar la segunta repeticion
def merge_the_tools(string,k):
    lista = []
    for i in range(0,len(string)):
        if i % k == 0:
            lista.append(string[i:i+k])
    newlista = []
    for i in lista:
        for i in list(i):
            if i not in newlista:
                newlista.append(i)
        newstring = ''.join(newlista)
        print(newstring)
        newlista = []
def run():
    string,k= input(), int(input())
    merge_the_tools(string,k)


run()
    

# AABCAAADA

