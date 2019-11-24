#Mostrar "Acceso denegado" mientras que la clave no sea la correcta
clave=""
clave_invalida=True

while(clave_invalida):
    clave=input("ingrese clave:")
    clave_invalida=(clave != "holamundo")
#fin del bucle
print("fin del bucle.")
