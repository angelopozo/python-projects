# 🏷️ Clases y Funciones en Python

## 🎯 Objetivos
- Entender qué es una clase y sus usos.
- Definir atributos y métodos, incluyendo `__init__`.
- Diferenciar funciones y métodos para modularizar código.
- Usar librerías estándar (`math`, `random`, `datetime`).

### Ejemplo de clase
```python
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)
```