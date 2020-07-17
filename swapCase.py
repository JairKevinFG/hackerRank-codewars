def run():
    n = input()
    swap_case(n)
def swap_case(n):
    lista= []
    array = list(n)
    for i in array:
        lista.append(i.upper())
    for i in range (0,len(lista)):
        if lista[i] == array[i]:
            lista[i]=lista[i].lower()
    string= ''.join(lista)
    print(string)
run()
