# Decodificar mensaje encriptado
# A = Hola
# B = Soy cesar
# C = Estudio en la unprg
# D = Tú donde estudias?
msg=(os.sys.argv[1])

for letra in msg:
    if letra == "A":
        print("Hola")
    if letra == "B":
        print("Soy cesar")
    if letra == "C":
        print("Estudio en la unprg ")
    if letra == "D":
        print("Tú donde estudias?")
#fin_iterador

print("Fin del bucle")
