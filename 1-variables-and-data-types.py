"""
--------------------------- VARIABLES / TIPOS DE DATOS ---------------------------
En este taller aprenderás cómo crear variables, trabajar con diferentes tipos de datos.
"""

"""
--- Ejercicio 1 Variables---
Crea una variable llamada "mensaje". 
Asígnale el valor "¡Hola, Mundo!". 
Imprime el valor de la variable en la consola.
"""
# Escribe tu código aquí
mensaje = "!Hola, Mundo!"
print(mensaje);

"""
--- Ejercicio 2 Variables---
Invoca la variable anterior llamada "mensaje". 
Reasígnale el valor "Hello world!". 
Imprime el valor de la variable en la consola.
Escribe en un comentario de línea lo que sucede.
"""
# Escribe tu código aquí
mensaje= "Hellow World!"
print(mensaje);
"""
--- Ejercicio 3 Tipos de datos---
Crea variables para cada uno de los siguientes tipos de datos y colecciones: string, int, float, 
bool, list, tuple, dicctionary and set. 
Imprime cada variable y el tipo de dato o colección que almacena en la consola.
"""
# Escribe tu código aquí
texto = "texto";
numero = 42;
flotante = 3.14;
booleano = True;
lista = [1, 2, 3];
tuple = (1, 2, 3);
diccionario = {"nombre": "Jorge", "edad": 25}
set = {1, 2, 3}

print(texto, type(texto));
print(numero, type(numero));
print(flotante, type(flotante));
print(booleano, type(booleano));
print(lista, type(lista));
print(tuple, type(tuple));
print(diccionario, type(diccionario));
print(set, type(set));