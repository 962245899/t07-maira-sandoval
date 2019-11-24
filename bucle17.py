#Decodificar mensaje encriptado
import  os
MSG=os.sys.argv[1].upper()


for letra in MSG:
    if letra == "o":
        print("hola")
    if letra =="i":
        print("como estas")
    if letra == "a":
        print("eres de la facultad?")
    if letra == "e":
        print("chau, cuidate")

#fin
print("\n")
print("fin del bucle")
