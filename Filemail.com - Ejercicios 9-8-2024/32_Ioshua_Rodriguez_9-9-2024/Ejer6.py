#Se ingresan tres valores por teclado, si todos son iguales se suma
#el primero por el segundo y se multiplica en resultado por el tercero
n1=int(input("Ingrese Numero: "))
n2=int(input("Ingrese Numero: "))
n3=int(input("Ingrese Numero: "))
if n1==n2 and n2==n1 and n3==n2:
    print(f"El resultado es: {(n1+n2)*n3}")
else:
    print("No son iguales")