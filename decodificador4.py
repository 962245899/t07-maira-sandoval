# decodificar mensaje encriptado
import os
#INPUT
msg=os.sys.argv[1]
# S = hola
# A = me gustaria verte
# E = lo se pero lo nuestro ya no va mas
# D = entiendo
msg="SAED"

for letra in msg :
    if letra == "S":
        print("hola")
    if letra == "A":
        print("me gustaria verte")
    if letra == "E":
        print("lo se pero lo nuestro ya no va mas")
    if letra == "D":
        print("entiendo")
    #fin_iterador

print("fin del bucle")
