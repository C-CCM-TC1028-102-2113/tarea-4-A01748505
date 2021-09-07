def main():
    #escribe tu código abajo de esta línea
    n=int(input())
    contador=0
    while n>=0:
        contador=contador+1
        if contador % 2 == 0:
            print(contador, "-%")
        else:
            print(contador, "-#")
        if contador>=n:
            break
    contador=contador+1
    pass

if __name__=='__main__':   
    main()
