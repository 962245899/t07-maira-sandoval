# decodificar mensaje encriptado
import os
#INPUT
msg=os.sys.argv[1]
# A = hola
# B = que haces
# E = aceptas salir conmigo
# F = claro que si
# G = entonces paso recogiendote
# R = esta bien
msg="ABEFGR"
for letra in msg :
    if letra == "A":
        print("hola")
    if letra == "B":
        print("que haces")
    if letra == "E":
        print("aceptas salir conmigo")
    if letra == "F":
        print("claro que si")
    if letra == "G":
        print("entonces paso recogiendote")
    if letra == "R":
        print("esta bien")
    #fin_iterador
print("fin del bucle")
