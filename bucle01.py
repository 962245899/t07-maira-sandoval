#validad la edad de un perro entre 0 y 18
edad=int(input("ingrese edad del perro:"))

edad_invalida=(edad<0 or edad >18)
#validad
while (edad_invalida==True):
    edad=int(input("ingrese edad del perro:"))
    edad_invalida=(edad<0 or edad >18)
#fin del while
print("fin del bucle")
