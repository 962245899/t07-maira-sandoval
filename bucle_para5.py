# La suma de numeros pares desde el 4 hasta el 10
import os
x=int(os.sys.argv[1])
i=4
suma=0
while(4>=i or i<=10):
    suma+=i
    i+= 2
#fin_while

print("La suma de numeros pares es:", suma)
