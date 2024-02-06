#Tuplas:
#Son "invariables", su estructura es similar a una lista, pero no tiene ningún método y siempre va en paréntesis.
#Las tuplas se mantienen constantes e invariables no se puede agregar, eliminar y modificar ninguno de sus elementos. 
my_tupla = ("Gerson", "Chaev", 2024, 170)
#my_tupla[3] = 250 #No es posible realizar esta acción
name, username, year, size = my_tupla

#Conversion de lista a tupla
my_list = ["Basilia","mamá"]
print(type(my_list))
my_list = tuple(my_list)
print(type(my_list))

print(f"Valor de la posicion 4 de la tupla: {my_tupla[3]}", f"\ntamanio de tupla es {len(my_tupla)}",end="\n")
print(f"Hello I am {name}, my username is {username}. This year is {year}. My size is {size/100} meters.")
