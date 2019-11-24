#Mostrar "Acceso denegado" mientras la clave ingresada no sea 12345
clave=""
clave_invalida=True

while (clave_invalida):
    clave=input("ingrese la clave:")
    clave_invalida=(clave != "12345")

#fin_while

print("Fin del bucle")
