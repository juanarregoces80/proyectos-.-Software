Python 3.10.12 (main, May 27 2025, 17:12:29) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> num1 = float(input("Ingresa el primer número: "))
... operacion = input("Ingresa la operación (+, -, *, /): ")
... num2 = float(input("Ingresa el segundo número: "))
... 
... if operacion == '+':
...     resultado = num1 + num2
... elif operacion == '-':
...     resultado = num1 - num2
... elif operacion == '*':
...     resultado = num1 * num2
... elif operacion == '/':
...     if num2 != 0:
...         resultado = num1 / num2
...     else:
...         resultado = "Error: División por cero"
... else:
...     resultado = "Operación no válida"
... 
... print("Resultado:", resultado)
