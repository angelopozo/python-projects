# 🐍 Tipos de Datos y Operadores en Python

## 🎯 Objetivos
- Conocer los tipos de datos básicos en Python: numéricos, booleanos y cadenas.  
- Aprender el uso de operadores aritméticos, de comparación, lógicos y especiales.  
- Realizar conversiones entre tipos de datos (casting).  
- Aplicar la entrada y salida de datos con `input()` y `print()`.  

---

## 1. Tipos de datos básicos
Python es un lenguaje de **tipado dinámico**: no hace falta declarar el tipo de la variable, se asigna automáticamente según el valor.

🔎 **La función `type()`**  
En Python, todo dato es un objeto de una determinada clase (entero, decimal, texto, etc.).  
La función integrada `type()` permite saber de qué tipo es una variable o un valor.

### Ejemplos
```python
# Enteros
a = 42
print(type(a))  # <class 'int'>

# Flotantes
b = 3.14
print(type(b))  # <class 'float'>

# Booleanos
c = True
print(type(c))  # <class 'bool'>

# Cadenas
d = "Hola, mundo"
print(type(d))  # <class 'str'>
```

## 2. Operadores aritméticos
- `+` suma
- `-` resta
- `*` multiplicación
- `/` división (flotante)
- `//` división entera
- `%` módulo (resto)
- `**` potencia

### Ejemplos
```python
x, y = 10, 3
print(x + y)   # 13
print(x - y)   # 7
print(x * y)   # 30
print(x / y)   # 3.333...
print(x // y)  # 3
print(x % y)   # 1
print(x ** y)  # 1000
```

## 3. Operadores de comparación
Devuelven valores booleanos (`True` o `False`).

- `==` igual
- `!=` distinto
- `<`, `<=`, `>`, `>=`

### Ejemplo
```python
print(5 == 5)   # True
print(5 != 3)   # True
print(5 < 10)   # True
print(10 >= 15) # False
```

## 4. Operadores lógicos
- `and` → Verdadero si ambas expresiones lo son.
- `or` → Verdadero si al menos una lo es.
- `not` → Niega el valor.

### Ejemplo
```python
x, y = True, False
print(x and y)  # False
print(x or y)   # True
print(not x)    # False
```

## 5. Operadores especiales
- **Identidad**: `is`, `is not` → comparan si dos variables apuntan al mismo objeto en memoria.
- **Pertenencia**: `in`, `not in` → verifican si un valor está dentro de una colección.

📌 **El tipo list (listas)**  
Una lista es una colección ordenada y modificable de elementos. Se escriben entre corchetes `[]`, separados por comas.

### Ejemplo
```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)     # True (misma referencia en memoria)
print(a is c)     # False (contenido igual pero distinto objeto)
print(2 in a)     # True
print(5 not in a) # True
```

## 6. Conversión de tipos (Casting)
Se usa para cambiar el tipo de una variable.

### Ejemplos
```python
# De cadena a número
x = int("10")
print(x + 5)  # 15

# De número a cadena
y = str(3.14)
print("El número es " + y)

# De flotante a entero
z = int(3.99)
print(z)  # 3
```

## 7. Entrada y salida de datos
- `input()` → lee datos como texto.
- `print()` → muestra resultados en pantalla.

### Ejemplo
```python
nombre = input("¿Cómo te llamas? ")
edad = int(input("¿Cuántos años tienes? "))
print("Hola", nombre, "tienes", edad, "años.")
```