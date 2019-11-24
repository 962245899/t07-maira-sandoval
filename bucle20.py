# Decodificar mensaje encriptado
# A = Hola
# B = Viste la final de la libertadores?
# C = en serio, yo no la vi
# D = estuve haciendo mi tarea de programacion
msg=(os.sys.argv[1])

for letra in msg:
    if letra == "A":
        print("Hola")
    if letra == "B":
        print("Viste la final de la libertadores?")
    if letra == "C":
        print("en serio, yo no la vi")
    if letra == "D":
        print("estuve haciendo mi tarea de programacion")
#fin_iterador

print("Fin del bucle")
