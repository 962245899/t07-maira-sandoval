# decodificar mensaje encriptado
# A = hola
# B = iras al paseo
# F = claro que si y tu
# G = yo no ire al paseo
# O = y porque
# T = tengo tareas por presentar
msg="ABFGOT"

for letra in msg :
    if letra == "A":
        print("hola")
    if letra == "B":
        print("iras al paseo")
    if letra == "F":
        print("claro que si y tu")
    if letra == "G":
        print("yo no ire al paseo")
    if letra == "O":
        print("y porque")
    if letra == "T":
        print("tengo tareas que presentar")
    #fin_iterador

print("fin del bucle")
