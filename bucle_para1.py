# La suma de los 150 primeros numeros
import os
#Input
x=int(os.sys.argv[1])
i=0
suma=0
while(i<=150):
    suma+=i
    i+= 1
#fin_while

print("La suma de los numeros es:", suma)
