d=int(input("Ingrese dia en numeros: "))
m=int(input("Ingrese Mes en numeros: "))
a=int(input("Ingrese año en numeros: "))
if m==1 or m==2 or m==3:
    if d<32 and a<2025:
        print("Es del primer trimestre del año")
        print(f"dia:{d} mes:{m} año:{a}")
    else:
        print("Dia o año no valido")