# 📘 README - Taller de Ejercicios de Programación en Python

Este documento describe cómo fueron abordados, resueltos y transpilados a Python los ejercicios entregados. Aquí se explican paso a paso las soluciones, especialmente aquellas que partían desde pseudocódigo o instrucciones escritas.

---

## 🔄 Transpilación de Algoritmos a Python

### 🧮 1. Cálculo de Pulsaciones por Ejercicio
**Problema:** Calcular el número de pulsaciones según edad y sexo.
- Se pidió edad y sexo al usuario.
- Según el sexo (M/F), se aplicó la fórmula correspondiente.
- Resultado mostrado con `print()`.

```python
edad = int(input("Indique su edad: "))
sexo = input("Indique su sexo (M o F): ")

if sexo.upper() == 'M':
    pulsaciones = (210 - edad) / 10
else:
    pulsaciones = (220 - edad) / 10

print(f"El número de pulsaciones es: {pulsaciones}")
```

### 💰 2. Inversión entre 3 personas
- Se capturaron tres montos de inversión.
- Se calculó el porcentaje individual respecto al total.

```python
inv1 = float(input("Inversión de la persona 1: "))
inv2 = float(input("Inversión de la persona 2: "))
inv3 = float(input("Inversión de la persona 3: "))

total = inv1 + inv2 + inv3
print(f"% persona 1: {inv1*100/total:.2f}%")
print(f"% persona 2: {inv2*100/total:.2f}%")
print(f"% persona 3: {inv3*100/total:.2f}%")
```

### 🏦 3. Interés de ahorro
- Se multiplicó el saldo inicial por el interés mensual (1.5%) por el número de meses.
- Resultado final mostrado.

```python
saldo = float(input("Ingrese el saldo inicial: "))
meses = int(input("Número de meses: "))
interes = saldo * 0.015 * meses
final = saldo + interes
print(f"Saldo final: {final}")
```

### 👷 4. Descuentos sobre sueldo base
- Se aplicaron porcentajes a un sueldo base.
- Cada descuento y el sueldo neto se imprimieron.

```python
sueldo = float(input("Sueldo base: "))
ley = sueldo * 0.01
seg_social = sueldo * 0.04
seg_forzoso = sueldo * 0.005
ahorro = sueldo * 0.05
neto = sueldo - (ley + seg_social + seg_forzoso + ahorro)

print(f"Caja ahorro: {ahorro}")
print(f"Ley política: {ley}")
print(f"Seguro forzoso: {seg_forzoso}")
print(f"Seguro social: {seg_social}")
print(f"Sueldo neto: {neto}")
```

### 📰 5. Costo de aviso clasificado
- Se usaron 3 multiplicaciones por cantidad de palabras, cm y colores.

```python
palabras = int(input("Palabras: "))
cm = int(input("Centímetros: "))
colores = int(input("Colores: "))

precio = palabras*20000 + cm*15000 + colores*25000
print(f"Precio total: ${precio}")
```

### 👴 6. Bono por antigüedad
- Se consideraron los años trabajados.
- Primer año: $100,000. Resto: $120,000 por año adicional.

```python
años = int(input("Años trabajados: "))
if años >= 1:
    bono = 100000 + (años - 1) * 120000
else:
    bono = 0
print(f"Bono a pagar: ${bono}")
```

---

## 🧠 Ejercicios de lógica básica (1 al 24)

Cada uno de los 24 ejercicios fue resuelto individualmente en archivos `.py`. A continuación, ejemplos de cómo se abordaron:

### 👶 Ejercicio 1: Clasificación de edad
```python
edad = int(input("Edad: "))
if edad <= 12:
    print("Niño")
elif edad <= 17:
    print("Adolescente")
elif edad <= 59:
    print("Adulto")
else:
    print("Adulto mayor")
```

### ➕ Ejercicio 2: Calculadora básica
```python
a = float(input("Número 1: "))
b = float(input("Número 2: "))
op = input("Operación (+ - * /): ")
if op == '+': print(a + b)
elif op == '-': print(a - b)
elif op == '*': print(a * b)
elif op == '/': print(a / b)
```

### 📝 Ejercicio 3: Notas
```python
nota = int(input("Nota (0-100): "))
if nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
elif nota >= 70:
    print("C")
elif nota >= 60:
    print("D")
else:
    print("F")
```
_(Y así sucesivamente hasta el ejercicio 24)_

---

## 📁 Estructura de entrega
```
Nombre-Completo/
├── ejercicio_01.py
├── ejercicio_02.py
├── ...
├── ejercicio_24.py
├── transpilados/
│   ├── ejercicio_pulsaciones.py
│   ├── ejercicio_inversiones.py
│   ├── ...
└── README.md
```

---

## 📝 Notas finales
- Todos los scripts están escritos en Python 3.
- Las soluciones están enfocadas en la lógica, entrada/salida y operaciones matemáticas básicas.
- Cada archivo fue probado individualmente.
- También se incluyó una versión manual escrita a mano como exige la entrega.

---

¡Gracias por revisar este proyecto! ✨
