
def main():
    #escribe tu código abajo de esta línea
    index = int(input("Enter the index: "))
    suma=0
    numero1=0
    numero2=1
    while index!=0 and index!=1:
        for i in range (1, index):
            suma=numero1+numero2
            numero1=numero2
            numero2=suma
        print (str(suma))
        break
    if index==0:
        print("0")
    elif index==1:
        print ("1")
    pass

if __name__=='__main__':
    main()
