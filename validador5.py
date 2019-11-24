# Ingresar el nombre de un dias
nombre_dias = ""
dias_invalida = True

while (dias_invalida):
    nombre_dias = input("ingrese el nombre_dias:")
    dias_invalida = (nombre_dias != "lunes" and nombre_dias != "martes" and nombre_dias != "miercoles" and nombre_dias != "jueves" and nombre_dias != "viernes" and nombre_dias != "sabado" and nombre_dias != "domingo")

# fin_while

print("Fin del bucle")
