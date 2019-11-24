#validar el nombre de un mes
nombre_de_un_mes=""
no_es_el_nombre_de_un_mes=True

while(no_es_el_nombre_de_un_mes):
    nombre_de_un_mes=input("Nombre de un mes:")
    no_es_el_nombre_de_un_mes=(nombre_de_un_mes != "enero" and nombre_de_un_mes != "febrero" and nombre_de_un_mes != "marzo" and nombre_de_un_mes != "abril" and nombre_de_un_mes != "mayo" and nombre_de_un_mes != "junio" and nombre_de_un_mes != "julio" and nombre_de_un_mes != "agosto" and nombre_de_un_mes != "setiembre" and nombre_de_un_mes != "octubre" and nombre_de_un_mes != "noviembre" and nombre_de_un_mes != "diciembre" )
#fin del bucle
print("fin")
