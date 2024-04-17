"""
Descubrimiento: En Python, los enteros y los flotantes no tienen límites específicos definidos por el lenguaje
en sí mismo, sino que dependen de la cantidad de memoria disponible en el sistema en el que
se ejecuta Python
"""

# Definición de variables de diferentes tipos primitivos
entero = 42
flotante = 3.14
cadena = "¡Hola, mundo!"
booleano = True

# Concatenación de las variables en una cadena, convirtiendo las no cadenas si es necesario
resultado = cadena + " El entero es " + str(entero) + ", el flotante es " + str(flotante) + ", y el booleano es " + str(booleano)

print(resultado)
# Límites de los enteros en Python:
# En Python, el tamaño de los enteros no está limitado por el número de bits, como en otros lenguajes de programación.
# Python 3.x tiene un tipo de entero llamado int, que puede representar enteros arbitrariamente grandes. 
# El límite viene dado por la memoria disponible en la máquina.
# Por ejemplo, en una máquina de 64 bits, el límite práctico puede ser el tamaño de la memoria disponible.

# Límites de los flotantes en Python:
# Python utiliza el estándar IEEE 754 para la representación de números de punto flotante.
# En Python, el tipo float representa números de punto flotante de doble precisión (64 bits).
# Los límites de los flotantes en Python están determinados por la precisión de la representación.
# El rango y la precisión dependen de la implementación de Python y la arquitectura subyacente.
# En general, Python puede manejar números de punto flotante con una precisión de aproximadamente 15 a 17 dígitos decimales.
# Los números demasiado grandes o pequeños pueden ser representados como infinito o cero respectivamente.
# Sin embargo, al realizar operaciones aritméticas, pueden ocurrir errores de redondeo debido a la precisión finita.
