# decodificar mensaje encriptado
import os
#INPUT
msg=os.sys.argv[1]
# A = hola
# B = que tal
# F = te estoy esperando
# R = chao
msg="ABFR"

for letra in msg :
    if letra == "A":
        print("hola")
    if letra == "B":
        print("que tal")
    if letra == "F":
        print("te estoy esperando")
    if letra == "R":
        print("chao")
    #fin_iterador

print("fin del bucle")
