# 📝 Cheatsheet: Tipos de Datos y Operadores en Python

## 🔢 Tipos de datos básicos
```python
int    # Entero
float  # Decimal
bool   # True / False
str    # Cadena de texto

type(x)  # Devuelve el tipo
```

### Ejemplo:
```python
a = 42
b = 3.14
c = True
d = "Hola"
```

## ➕ Operadores aritméticos
| Operador | Descripción         | Ejemplo    | Resultado |
|----------|---------------------|------------|-----------|
| `+`      | Suma                | `10 + 3`   | 13        |
| `-`      | Resta               | `10 - 3`   | 7         |
| `*`      | Multiplicación      | `10 * 3`   | 30        |
| `/`      | División flotante   | `10 / 3`   | 3.333...  |
| `//`     | División entera     | `10 // 3`  | 3         |
| `%`      | Módulo (resto)      | `10 % 3`   | 1         |
| `**`     | Potencia            | `10 ** 3`  | 1000      |

## ⚖️ Operadores de comparación
| Operador | Ejemplo       | Resultado |
|----------|---------------|-----------|
| `==`     | `5 == 5`      | `True`    |
| `!=`     | `5 != 3`      | `True`    |
| `<`      | `5 < 10`      | `True`    |
| `>=`     | `10 >= 15`    | `False`   |

## 🔗 Operadores lógicos
| Operador | Uso                  | Ejemplo            | Resultado |
|----------|----------------------|--------------------|-----------|
| `and`    | Ambas verdaderas     | `True and False`   | `False`   |
| `or`     | Al menos una         | `True or False`    | `True`    |
| `not`    | Niega valor          | `not True`         | `False`   |

## ✨ Operadores especiales
- **Identidad**: `is`, `is not`
- **Pertenencia**: `in`, `not in`

### Ejemplo:
```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)   # True
print(a is c)   # False
print(2 in a)   # True
```

## 🔄 Casting
```python
int("10")
str(3.14)
int(3.99)
```

## ⌨️ Entrada y salida
```python
nombre = input("¿Cómo te llamas? ")
edad = int(input("¿Edad? "))
print("Hola", nombre, "tienes", edad, "años.")
```

## 📌 Tip rápido
Usa help() o dir() para explorar funciones y métodos disponibles.
