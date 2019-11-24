#La suma de los 50 primeros sumandos
import os
x=int(os.sys.argv[1])
i=0
suma=0
while(i<=x):
    suma+=i
    i+=1
#fin
print("La suma de los numeros es:", suma)
