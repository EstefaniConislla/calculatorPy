import math
# Declaro
while 1:
    num1= float(input("ingresa el primer valor: "))
    num2= float(input("ingresa el segundo valor: ")) 

    # Realizo
    print("Seleccione la operación a realizar: ")
    print("1, suma")
    print("2, resta")
    print("3, multipliocación")
    print("4, división")
    print("5, potencia")
    print("6, logaritmo(logaritmo del primer número [num1]")

    n= int(input("¿Cuál opción quiere? "))

    if n==1:
        res= num1+num2
        print("su resultado es de: ", res)
    elif n==2:
        res= num1-num2
        print("su resultado es de: ", res)
    elif n==3:
        res= num1*num2
        print("su resultado es de: ", res)
    elif n==4 and num2!=0:
        res= num1/num2
        print("su resultado es de: ", res)
    elif n==5:
        res= num1**num2
        print("su resultado es de: ", res)
    elif n==6 and num1>0:
        res= math.log10(num1)
        print("su resultado es de: ", res)
    else:
        print("Opción desconocida")