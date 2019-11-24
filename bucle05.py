#Mostrar "Acceso denegado" mientras que la clave no sea "si" o "no"
de_que_equipo_eres=""
final=True

while(final):
    de_que_equipo_eres=input("De que equipo eres(al/u):")
    final=(de_que_equipo_eres != "al" and de_que_equipo_eres != "u")
#fin del bucle
print("Fin del bucle.")
