#La suma de los x primeros sumandos impares
import os
x=int(os.sys.argv[1])
i=0
suma=0
while(i<=x):
    suma+=i
    i+=3
#fin
print("La suma de los numeros es:", suma)
