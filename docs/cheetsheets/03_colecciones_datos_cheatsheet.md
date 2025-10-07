# 📝 Cheatsheet: Colecciones de Datos en Python

## 📋 Listas
```python
lst = [1, 2, 3]
lst.append(4)
lst.insert(1, 99)
lst.remove(2)
x = lst.pop()
lst.sort()
lst.reverse()
sub = lst[1:4]
```

## 🧩 Tuplas
```python
t = (1, 2, 3)
x, y, z = t
# Inmutable
```

## 🔹 Conjuntos
```python
s = {1, 2, 3}
s.add(4)
s.remove(2)
print(s | {3, 5})  # unión
print(s & {3, 5})  # intersección
```

## 🗂️ Diccionarios
```python
d = {"nombre": "Ana", "edad": 25}
d["edad"] = 26
d.get("correo", "sin correo")
del d["edad"]
for k, v in d.items():
    print(k, v)
```

## ⚡ Comprensiones
```python
[x**2 for x in range(5)]
{c for c in "python" if c not in "aeiou"}
{x: x**2 for x in range(5)}
```

## 💡 Tip rápido
Usa set() para eliminar duplicados y dict.get() para evitar errores de clave.
