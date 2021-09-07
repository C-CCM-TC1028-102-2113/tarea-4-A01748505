def main():
    #escribe tu código abajo de esta línea
    cont=0
    sum=0
    num=float(input())
    while num>=0:
        sum=sum+num
        cont=cont+1
        num=float(input())
        if num<0:
            break
    promedio=sum/cont
    print(promedio)
    pass
if __name__=='__main__':
    main()
