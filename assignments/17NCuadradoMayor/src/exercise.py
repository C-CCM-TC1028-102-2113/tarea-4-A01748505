def main():
    #Escribe tu código debajo de esta línea
    num=int(input("Escribe un numero : "))
    contador=1
    while (contador**2)<=num:
        contador=contador+1
    print (contador)
    pass

if __name__=='__main__':
    main()
