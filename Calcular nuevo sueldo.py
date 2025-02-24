s=int(input("Ingrese su sueldo: "))
a=int(input("Ingrese años de antiguedad: "))
if s<500 and a>=10:
    print(f"Su sueldo sera de:{(round(s*0.20))+s}")
elif s<500 and a<10:
    print(f"Su sueldo sera de:{(round(s*0.05))+s}")
elif s>=500:
    print(f"Su sueldo sera de:{s}")