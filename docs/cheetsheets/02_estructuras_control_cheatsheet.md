# 📝 Cheatsheet: Estructuras de Control en Python

## ✅ Condicionales
```python
if condicion:
    # código
elif otra_condicion:
    # código
else:
    # código
```

### Expresión condicional (ternario)
```python
mensaje = "par" if numero % 2 == 0 else "impar"
```

### match (Python 3.10+)
```python
match estado:
    case 400: print("Petición incorrecta")
    case 404: print("No encontrado")
    case _:   print("Error desconocido")
```

## 🔄 Bucles for
```python
for elemento in iterable:
    # código

for i in range(1, 10, 2):
    print(i)

for i, valor in enumerate(lista):
    print(i, valor)

for a, b in zip(lista1, lista2):
    print(a, b)
```

## 🔁 Bucles while
```python
while condicion:
    # código
else:
    print("Fin")
```

## ⚡ Control de bucles
- break: sale del bucle.
- continue: salta a siguiente iteración.
- else: ejecuta si no hubo break.
- pass: marcador vacío.

## ⚠️ Manejo de errores
```python
try:
    # código
except ValueError:
    print("Error de valor")
else:
    print("Sin errores")
finally:
    print("Siempre se ejecuta")
```

## 💡 Tip rápido
Usa enumerate() y zip() para escribir bucles más legibles.
