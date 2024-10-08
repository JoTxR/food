import math
import random
import matplotlib.pyplot as mplot
import pandas as pd
from itertools import product

def conjuntos(potencia):
    for x in range(potencia+1):
        print(x)
        for combo in product('01', repeat=x):
            y = ''.join(combo)
            salida.write(", " + y)  # Escribe en UniversoK.txt
            salida2.write(str(y.count("1")) + "\n")  # Escribe la cantidad de unos por cadena en contadorunos.txt
            salida3.write(str(y.count("0")) + "\n")  # Escribe la cantidad de ceros por cadena en contadorceros.txt
            # Manejar los casos en los que el conteo sea 0 para evitar log(0)
            if y.count("1") > 0:
                salida4.write(str(math.log10(y.count("1"))) + "\n")
            else:
                salida4.write("0\n")  # Evita error en logaritmo

            if y.count("0") > 0:
                salida5.write(str(math.log10(y.count("0"))) + "\n")
            else:
                salida5.write("0\n")  # Evita error en logaritmo
# Funcion graficadora de unos
def graficar1():
    data = pd.read_csv('contadorunos.txt', header=0, delim_whitespace=True)
    mplot.title("Grafica de unos")
    mplot.xlabel("Conjuntos")
    mplot.ylabel("No. 1's")
    mplot.grid(True)
    mplot.plot(data, "g")
    mplot.show()

# Funcion graficadora de ceros
def graficar2():
    data = pd.read_csv('contadorceros.txt', header=0, delim_whitespace=True)
    mplot.title("Grafica de ceros")
    mplot.xlabel("Conjuntos")
    mplot.ylabel("No. 0's")
    mplot.grid(True)
    mplot.plot(data, "r")
    mplot.show()

# Funcion graficadora de log10
def graficar3():
    data = pd.read_csv('logceros.txt', header=0, delim_whitespace=True)
    mplot.title("Grafica de unos en logaritmo")
    mplot.xlabel("Conjuntos")
    mplot.ylabel("No. 0's")
    mplot.grid(True)
    mplot.plot(data, "g")
    mplot.show()

# Funcion graficadora de log10
def graficar4():
    data = pd.read_csv('logunos.txt', header=0, delim_whitespace=True)
    mplot.title("Grafica de ceros en logaritmo")
    mplot.xlabel("Conjuntos")
    mplot.ylabel("No. 0's")
    mplot.grid(True)
    mplot.plot(data, "r")
    mplot.show()


def menu():
    print("Deseas ingresar manualmente un k menor a 1000? Si / No")
    opc = input()

    if opc == "No" or opc == "no":
        k = random.randint(1, 1000)
        print("Se obtendra el universo con K igual a ", k)
    else:
        print("Indique el valor de K por favor")
        k = int(input())

    # Escritura de datos

    salida.write("\u03A3 = { \u03B5 ")  # Escribe los primeros simbolos en UniversoK.txt
    conjuntos(k)  # Envia la potencia de 2 a la K al metodo conjuntos
    salida.write("}")  # Escribe el ultimo caracter en UniversoK.txt
    salida2.close()
    salida3.close()
    salida4.close()
    salida5.close()

    graficar1()
    graficar2()
    graficar3()
    graficar4()

salir = "N"
while salir != "S":
    salida = open("UniversoK.txt", "w", encoding="utf-8")
    salida2 = open("contadorunos.txt", "w")
    salida3 = open("contadorceros.txt", "w")
    salida4 = open("logceros.txt", "w")
    salida5 = open("logunos.txt", "w")
    menu()
    salir = input("Deseas salir? [S/N]\n")
