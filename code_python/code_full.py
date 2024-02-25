""" 
       #TUPLAS
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

        #DICCIONARIOS
tupla = ("primero",2)
myDictionary = {"name":"Gerson",14:"My birthday", "day":[14,"Enero","Ate"],tupla[1]: "Prueba de tupla"}
print(myDictionary[14], myDictionary["day"])
myDictionary["hobby"] = "baketball" #Agregando
myDictionary["day"][2] = "Lima" #Modificando
del myDictionary["name"] #Eliminando
print(myDictionary)
#Metodos del diccionario
print(myDictionary.keys())
print(myDictionary.values())

        #CONDICIONALES
list_courses = ("calculo","estadistica","IA")

election = input("Ingrese curso: ")

if election.lower() in list_courses: # or .upper()
    print("El curso es "+str(election.lower()))
else:
    print("El curso "+str(election.lower())+" no existe")

        #BUCLES
email = input("Ingrese su correo: ")

msg1, msg2 = "No hay @", "No hay ."

for i in email: #recorre cadenas, tuplas, listas, etc
    if i == "@":
        msg1 = "hay @"
    elif i == ".":
        msg2 = "hay ."
    else:
        msg3 = "by Gerson"

for i in range(1,10,2): #(inicio, fin-1, deCuantoEnCuanto)
    print(f"{i} \t {msg1} \t {msg2} \t {msg3}")

        #FUNCIONES CONTINUE, PASS, BREAK
msg = "Prueba"
for i in "Gerson":
    if i == "r":
        continue #continue: ignora el código que le sigue y salta a lo siguiente.
        estoNoFunciona
        print("Hola mundo")
        msg = "este es un mensaje"
    print(str(i)+"\t"+str(msg))
####################################
class carrito:
    pass #Es como si el código no existiese. Lo ignora totalmente. Permite crear funciones, clases, etc vacías
                    #y asi evitar errores de sintaxis

####################################
word = input("Ingresa palabra: ")

for i in word:
    if i == "g":
        band = True
        break #break: rompe el programa o permite salir de un bucle. 
        print("saliooo") #no lo lee porque ya salió con el break
else:
    band = False

print(band)


        #GENERADORES
#Retornan de 1 en 1 los datos por medio de next() y ahorran memoria.
def devuelve_potencias(num):
    for i in range(num):
        yield (i+1)**2

potencias = devuelve_potencias(3) #es necesario para almacenar la data

print(next(potencias)) #1
print(next(potencias)) #4
print(next(potencias)) #9

#USO del yield from (para acceder a un subelemento)
def return_words(*parameters): #El "*" indica que puede ser "n" parametros
    for subElement in parameters: #Accediendo a elementos
        yield from subElement #Retornando cada subelemento 

result = return_words(["Gerson","chaev"], "Basilia", (15,28)) 

print(next(result)) #Gerson
print(next(result)) #Chaev
print(next(result)) #B

        #EXCEPCIONES
def operation():
    try:
        num1 = int(input("num1: "))
        num2 = int(input("num2: "))
        return (num1/num2)
    except ValueError: #Los errores de excepción lo bota la consola
        print("Ingresó un dato no numérico")
    except ZeroDivisionError:
        print("No es posible dividir entre 0")
    finally: 
        print("'Finally' siempre se ejecuta, pese a todo")

print("Solución: "+str(operation()))
print("Fin programa")

#Uso del RAISE(provocar una excepcion)
def eres_mayor(age):
    if age<0:
        raise ValueError("No hay edad negativa") #provocando excepcion
    else:
        if age<18:
            print("Eres menor")
        else:
            print("Eres mayor")

dato = int(input("Ingresa dato: "))

try:
    print(eres_mayor(dato))
except ValueError as Edad_negativa: #alias de la excepcion
    print(Edad_negativa)

print("End program")

"""
            #POO
#Clase: Define la forma de un objeto.
#Objeto: Instancia de una clase. Tiene atributos y metodos.
#Encapsulamiento: Solo permite usar atributos y metodos dentro de la clase
#Constructor: Estado inicial de todos los objetos que se creen.

class Dog():
    state = ""

    def __init__(self, color, size): #constructor
        self.__name = "" #encapsulamiento del atributo name -> "__"
        self.color = color 
        self.size = size
        self.age = ""
        self.weight = 0

    def print_data(self):
        print("El perro se llama ",self.__name," su color es ",self.color," y su tamanio es ",self.size," y es ", self.age)

    def colocar_nombre(self,name): #Setter: Estableciendo valor a un atributo encapsulado
        self.__name = name

    def obtener_nombre(self): #Getter: Obteniendo valor de un atributo encapsulado
        return self.__name
    
    def __state_salud(self,weight): #Método encapsulado -> "__"
        if(weight>20):
            self.state ="sobrepeso"
        else:
            self.state ="saludable"
        return self.state

    def info_dog(self,solicitud):
        if(solicitud):
            return self.__state_salud(self.weight) #llamando metodo encapsulado

dog1 = Dog("negro","mediano") #instancia de "Dog"
dog1.__name = "pulpito" #Por el encapsulamiento no es posible modificarlo
print("###################################")
dog1.print_data() 
dog1.colocar_nombre("Bombom") #Usando setter para colocar nombre
print("###################################")
print("El nombre del perrito es ",
dog1.obtener_nombre()) #Usando getter para obtener nombre
dog1.age = "adulto"
dog1.print_data() 
print("##############Estado#####################")
dog1.weight = (int)(input("Ingrese peso: "))
print("Estado: ",dog1.info_dog(input("Info (True): ")))