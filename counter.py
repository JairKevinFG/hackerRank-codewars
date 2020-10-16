

def run():
    nro_zap= int(input())
    tallas = input().split()
    list_tallas = list(map(int,tallas))
    nclientes = int(input())
    costototal = venta(nro_zap,list_tallas,nclientes)
    print(costototal)

def venta(nro_zap,list_tallas,nclientes):
    costototal = 0
    i = 0
    while (i< nclientes):
        i=i+1
        tall,precio=input().split()
        if int(tall) in list_tallas:
            index= list_tallas.index(int(tall))
            del list_tallas[index]
            costototal = costototal + int(precio)
    return costototal

run()
