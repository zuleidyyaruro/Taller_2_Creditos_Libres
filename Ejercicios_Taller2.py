# --------------------------- Crear un diccionario con los elementos nombre, cedula, carrera y
# ---------- Por medio de entrada de texto mencione que elemto se quiere editar y anadirlo al diccionario
diccionario=[
    {
        'nombre':'Antonio',
        'cedula':'123456',
        'carrera':'Sistemas'
    }
]

elemento=(input("Qué elemento desea cambiar"))

if(elemento=='nombre'):
    nombre=(input("Ingrese el nombre: "))
    diccionario[0]['nombre']=nombre
elif(elemento=='cedula'):
    cedula=(input("Ingrese la cedula: "))
    diccionario[0]['cedula']=cedula
elif(elemento=='carrera'):
    carrera=(input("Ingrese la carrera: "))
    diccionario[0]['carrera']=carrera

print("\nListado de contactos: ")
print("---------------------------------")

for i in diccionario:
    print(f"Nombre: {i['nombre']}")
    print(f"Cedula: {i['cedula']}")
    print(f"Carrera: {i['carrera']}")
    print("---------------------------------")


# -------------------------------Ejercicio 1-----------------------------------------

print("****Funcion que recorra la lista y devuelva strings")

listaNumeros=[1, 80, 515,21, 2, 10, 28, 15]

def funcionLista():
    for numeros in listaNumeros:
        print(f"{listaNumeros.index(numeros)+1}. {numeros}")

print(funcionLista())

print()

print("****Lista de Peliculas Ordenada****")
listaNumeros.sort()
print(listaNumeros)

print()
print("****Mostrar Longitud*****")

longitud=len(listaNumeros)
print(f"La longitud de la lista es: {longitud}")

print()
print("*******Buscar elemento en la lista*******")

buscar=(input("Ingrese el elemento que desea buscar: "))


if buscar in listaNumeros:
    print(f"El numero {buscar} sí se encuentra en la lista")
else:
    print(f"El numero {buscar} no se encuentra en la lista")


# ---------------------- Ejercicio 2 ----------------------------------------

listaNumeros=[]
n=0

longitud=len(listaNumeros)

while n<120:

    numero=int(input("Ingrese el nuevo numero: "))
 
    listaNumeros.append(numero)
    n=n+1

print()
print("Lista de numeros")

for i in listaNumeros:
    print(i)

# --------------------------Ejercicio 3 -------------------------------------------

variable1=None

if(variable1==None):

    variable1=(input("Ingrese texto en minuscula: "))
    variableMayuscula=variable1.upper()

    print(f"Texto en mayuscula: {variableMayuscula}")

# ---------------------------Ejercicio 4----------------------------------------

def tipoDato():


    lista=["Esto", "Es", "Una", "Lista"]
    caracter="A"
    entero=2020
    booleano=True

    print(f"Tipo de dato: {type(lista)}")
    print(f"Tipo de dato: {type(caracter)}")
    print(f"Tipo de dato: {type(entero)}")
    print(f"Tipo de dato: {type(booleano)}")

tipoDato()

# -----------------------------Ejercicio 5-----------------------------

accion=  ["GTA","COD","PUGB"]
aventura=["ASSINS","CRASH","Prince Of Persia"]
deportes=["FIFA 21","PRO 21","MOTO GP 21"]

accion.sort()
aventura.sort()
deportes.sort()

print(f" ACCION   : {accion}")
print(f" AVENTURA : {aventura}")
print(f" DEPORTES : {deportes} ")
