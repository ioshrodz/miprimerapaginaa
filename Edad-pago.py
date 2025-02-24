e=int(input("Ingrese su edad: "))
if e<4:
    print("No requiere pago(Gratis)")
elif e<18:
    print("El pago requerido es de 100LPS")
elif e>17 and e<100:
    print("El pago requerido es de 200LPS")
elif e<0 or e>100:
    print("Edad no Valida")