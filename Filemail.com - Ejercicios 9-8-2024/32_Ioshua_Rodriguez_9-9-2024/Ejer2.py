p=int(input("1.Vegetariana 2.No Vegetariana: "))
if p==1:
    i=int(input("Ingredientes: 1.Pimiento 2.Tofu: "))
    if i==1:
        print("Pizza Vegetariana","Ingrediente: Pimiento")
    elif i==2:
        print("Pizza Vegetariana","Ingrediente: Tofu")
    else:
        print("Ingrediente no Valido")
elif p==2:
    i=int(input("Ingredientes: 1.Peperoni 2.Jamon 3.Salmon: "))
    if i==1:
        print("Pizza No Vegetariana","Ingrediente: Peperoni")
    elif i==2:
        print("Pizza No Vegetariana","Ingrediente: Jamon")
    elif i==3:
        print("Pizza No Vegetariana","Ingrediente: Salmon")
    else:
        print("Ingrediente no Valido")