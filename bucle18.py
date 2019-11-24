# Decodificar mensaje encriptado
# A = Hola
# B = Eres de 2do ciclo
# F = Ayudame con mis tareas
# R = Gracias
msg=os.sys.argv[1].upper()

for letra in msg:
    if letra == "A":
        print("Hola")
    if letra == "B":
        print("Eres de 2do ciclo")
    if letra == "F":
        print("Ayudame con mis tareas")
    if letra == "R":
        print("Gracias")
#fin_iterador

print("Fin del bucle")
