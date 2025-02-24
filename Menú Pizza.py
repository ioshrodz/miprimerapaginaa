e=int(input("1.Vegetariana, 2.No Vegetariana: "))
if e==1:
    i=int(input("Ingrediente: 1.Pimiento, 2.Tofu: "))
    if i==1:
        print("Pizza Vegetariana");print("Ingrediente: Pimiento")
    elif i==2:
        print("Pizza Vegetariana");print("Ingrediente: Tofu")
    else:
        print("Ingrediente No Valido")
elif e==2:
    i=int(input("Ingrediente: 1.Peperoni 2.Jamon 3.Salmon: "))
    if i==1:
        print("Pizza No Vegetariana");print("Ingrediente: Peperoni")
    elif i==2:
        print("Pizza No Vegetariana");print("Ingrediente: Jamon")
    elif i==3:
        print("Pizza No Vegetariana");print("Ingrediente: Salmon")
    else:
        print("Ingrediente No Valido")
else:
    print("Pizza No Valida")
