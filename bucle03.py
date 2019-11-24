#Mostrar "Acceso denegado" mientras que la clave no sea "si" o "no"
desea_continuar=""
no_desea_continuar=True

while(no_desea_continuar):
    desea_continuar=input("Desea continuar(si/no):")
    no_desea_continuar=(desea_continuar != "si" and desea_continuar != "no")
#fin del bucle
print("Fin del bucle.")
