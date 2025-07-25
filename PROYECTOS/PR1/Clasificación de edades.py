Python 3.10.12 (main, May 27 2025, 17:12:29) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> edad = int(input("Ingresa tu edad: "))
... 
... if edad >= 0 and edad <= 12:
...     print("Eres un Niño.")
... elif edad <= 17:
...     print("Eres un Adolescente.")
... elif edad <= 59:
...     print("Eres un Adulto.")
... else:
...     print("Eres un Adulto mayor.")
