temperatura=float(input("ingrese temperatura:"))
print(temperatura)

temperatura_invalida=(temperatura < 34.0 or temperatura > 39.0)

#validar que la temperatura este entre 34.0 y 39.0
while (temperatura_invalida==True):
    temperatura=float(input("ingrese la temperatura"))
    temperatura_invalida=(temperatura< 34.0 or temperatura > 39.0)
#fin_while

print("Fin del bucle")
