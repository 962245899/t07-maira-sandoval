#Mostrar "Acceso denegado" mientras la respuesta ingresada no sea si o no
desea_continuar=""
desea_continuar_invalida=True

while (desea_continuar_invalida):
    desea_continuar=input("ingrese la desea_continuar:")
    desea_continuar_invalida=( desea_continuar != "si" and desea_continuar !="no")

#fin_while

print("Fin del bucle")
