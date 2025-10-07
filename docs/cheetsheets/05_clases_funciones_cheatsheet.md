# 📝 Cheatsheet: Clases y Funciones en Python

## 🏷️ Definir una clase
```python
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mover(self, dx, dy):
        self.x += dx
        self.y += dy
```

## ⚡ Crear objeto
```python
p = Punto(3, 4)
p.mover(1, 2)
```

## 🔧 Funciones
```python
def sumar(a, b=0):
    return a + b

print(sumar(5))
```

## 🛠️ Librerías útiles
```python
import math, random, datetime

math.sqrt(16)
random.randint(1, 6)
datetime.datetime.now()
```

## 💡 Tips rápidos
- Usa docstrings con tres comillas para documentar.
- Las funciones son objetos de primera clase: se pueden pasar como argumentos.
