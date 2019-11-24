edad=int(input("ingrese edad:"))
print(edad)

edad_invalida=(edad < 0 or edad > 100)

#validar que la edad este entre 0 y 100
while (edad_invalida==True):
    edad=int(input("ingrese la edad"))
    edad_invalida=(edad < 0 or edad > 100)
#fin_while

print("Fin del bucle")

