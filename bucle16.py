#La suma de los numeros impares desde el 0 hasta el x
import os
x=int(os.sys.argv[1])

suma=0
while(0>=x or x<=10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 ):
    suma+=x
    x+=3
#fin

print("la suma de los numeros impares es:", suma)
