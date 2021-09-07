
def main():
    #Escribe tu código debajo de esta línea
    height=int(input("Enter triangle height: "))
    for i in range (height+1): 
        if i==0:
            i=i+1
        elif i!=0:
            blancos=height-i
            print(' '*blancos+'*'*i)
    pass


if __name__=='__main__':
    main()
