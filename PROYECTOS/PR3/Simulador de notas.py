Python 3.10.12 (main, May 27 2025, 17:12:29) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> nota = int(input("Ingresa la nota (0-100): "))
... 
... if 90 <= nota <= 100:
...     print("Calificación: A")
... elif 80 <= nota < 90:
...     print("Calificación: B")
... elif 70 <= nota < 80:
...     print("Calificación: C")
... elif 60 <= nota < 70:
...     print("Calificación: D")
... elif 0 <= nota < 60:
...     print("Calificación: F")
... else:
...     print("Nota inválida")
