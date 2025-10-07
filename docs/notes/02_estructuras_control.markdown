# 🧭 Estructuras de Control en Python

## 🎯 Objetivos
- Dominar las **instrucciones condicionales** y comprender que Python basa su sintaxis en la **sangría**, no en llaves ni paréntesis.  
- Repetir tareas con **bucles `for` y `while`**, incluyendo técnicas de iteración como `range()`, `enumerate()` y `zip()`, y comprender cómo **interrumpir o continuar** la ejecución.  
- Gestionar el flujo de ejecución cuando ocurren errores mediante **bloques `try/except/else/finally`** y aprender a lanzar excepciones propias.  
- Conocer nuevas construcciones de control como la **expresión condicional en línea** y la sentencia **`match`** introducida en Python 3.10.  

---

## 1. Condicionales

Las **sentencias condicionales** permiten ejecutar bloques de código solo si se cumple una condición.  
En Python **no se usan paréntesis ni llaves** como en otros lenguajes; la sintaxis se basa en palabras clave y **sangría obligatoria**.

- `if` → Evalúa una condición y ejecuta el bloque si es verdadera.  
- `elif` (else if) → Comprueba condiciones adicionales si la anterior no se cumplió.  
- `else` → Se ejecuta cuando ninguna condición anterior fue verdadera.  
- `:` → Indica el inicio del bloque de código dependiente.  
- **Indentación** → Fundamental en Python, define el alcance de cada bloque.

### Ejemplo
```python
edad = 18

if edad < 12:
    print("Eres un niño")
elif edad < 18:
    print("Eres adolescente")
elif edad < 65:
    print("Eres adulto")
else:
    print("Eres mayor")
```

### Expresión condicional (operador ternario)
Permite escribir condiciones simples en una sola línea:

```python
mensaje = "par" if numero % 2 == 0 else "impar"
```

Equivale a `condición ? valor_si_verdadero : valor_si_falso` en otros lenguajes.

### Sentencia `match` (Python 3.10+)
Permite comparar un valor contra varios **patrones**, similar a `switch` pero más potente.

```python
def http_error(status):
    match status:
        case 400:
            return "Petición incorrecta"
        case 404:
            return "No encontrado"
        case 418:
            return "Soy una tetera"
        case _:
            return "Error desconocido"
```

- `_` actúa como comodín.  
- Soporta desempaquetado de tuplas y objetos.

---

## 2. Bucles

### 🔄 Bucle `for`
En Python, `for` **itera sobre elementos** de una secuencia (listas, tuplas, cadenas, diccionarios, etc.) sin necesidad de índices manuales.

- `range(fin)` → Números de `0` a `fin-1`.  
- `range(inicio, fin, paso)` → Controla inicio y salto.  
- `enumerate()` → Devuelve índice y valor en cada iteración.  
- `zip()` → Itera varias colecciones a la vez.

#### Ejemplos
```python
# Iterar una lista
nombres = ["Ana", "Luis", "Sofía"]
for nombre in nombres:
    print(nombre.upper())

# Con range
for i in range(5):      
    print(i)

# Con inicio y paso
for i in range(1, 10, 2):  
    print(i)

# enumerate
for indice, valor in enumerate([10, 20, 30]):
    print(f"Índice {indice}: {valor}")

# zip
nombres = ["Ana", "Luis", "Sofía"]
edades  = [20, 22, 19]
for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")
```

### ⚡ Control de bucles
- `break` → Sale inmediatamente del bucle actual.  
- `continue` → Salta a la siguiente iteración.  
- `else` → Se ejecuta si el bucle termina sin `break`.  
- `pass` → No hace nada, útil como marcador de código pendiente.

```python
# Buscar número primo con for-else
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} es igual a {x} × {n//x}")
            break
    else:
        print(f"{n} es un número primo")

# Uso de continue
for num in range(2, 10):
    if num % 2 == 0:
        print(f"Encontrado par {num}")
        continue
    print(f"Encontrado impar {num}")
```

### 🔁 Bucle `while`
Repite su cuerpo mientras la condición sea verdadera.

```python
x = 5
while x > 0:
    print(x)
    x -= 1
else:
    print("¡Despegue!")
```

- Útil para procesos de duración indeterminada.
- También admite `else`, `break`, `continue` y `pass`.

---

## 3. Manejo de errores

En Python, los **errores de sintaxis** detienen el programa antes de ejecutarse, mientras que las **excepciones** ocurren durante la ejecución y pueden ser capturadas.

### Bloques `try/except`
Permiten manejar errores específicos y evitar que el programa se detenga.

```python
try:
    num = int(input("Introduce un número: "))
    resultado = 10 / num
except ZeroDivisionError:
    print("No puedes dividir entre 0")
except ValueError:
    print("Debes introducir un número válido")
except (TypeError, NameError):
    print("Otro tipo de error")
else:
    print(f"El resultado es {resultado}")  # solo si no hubo excepción
finally:
    print("Ejecución finalizada")  # siempre se ejecuta
```

- `try` → Bloque que puede fallar.  
- `except` → Captura errores específicos.  
- `else` → Se ejecuta solo si no hubo excepción.  
- `finally` → Siempre se ejecuta (para limpieza de recursos, mensajes finales, etc.).

---

✅ **En resumen:**  
Con las **estructuras de control**, puedes dirigir el flujo de tu programa, repetir tareas y manejar errores de forma segura y clara.  
Dominar `if/elif/else`, `for`, `while` y el manejo de excepciones hará tu código más robusto y legible.

---