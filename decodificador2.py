# decodificar mensaje encriptado
import os
#INPUT
msg=os.sys.argv[1]
# A = hola
# B = que tal
# F =  te extraño
# R = yo tambien
msg="ABFR"

for letra in msg :
    if letra == "A":
        print("hola")
    if letra == "B":
        print("que tal")
    if letra == "F":
        print("te extraño")
    if letra == "R":
        print("yo tambien")
    #fin_iterador

print("fin del bucle")
