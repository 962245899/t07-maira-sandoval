#La suma de los numeros pares desde el 10 hasta el x
import os
x=int(os.sys.argv[1])

suma=0
while(10>=x or x<=10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 ):
    suma+=x
    x+=2
#fin

print("la suma de los numeros impares desde el 10 es:", suma)
