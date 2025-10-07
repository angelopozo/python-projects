# 📦 Colecciones de Datos en Python

## 🎯 Objetivos de la unidad
- Conocer y manipular listas, tuplas, conjuntos y diccionarios.
- Usar operaciones básicas de inserción, búsqueda y borrado.
- Crear listas dinámicas con list comprehensions.

## 1. Listas
Las listas (**list**) son secuencias mutables que permiten almacenar cualquier tipo de dato y cuyo tamaño puede crecer o disminuir dinámicamente. Los índices comienzan en 0 y se admiten índices negativos para contar desde el final (-1 es el último elemento). Además de acceder a un elemento concreto, el *slicing* (`lista[inicio:fin:paso]`) permite extraer sublistas sin bucles explícitos.

### Operaciones principales
- **Añadir elementos**: `append(x)` agrega `x` al final; `extend(iterable)` concatena otra colección; `insert(i, x)` inserta `x` antes del índice `i`.
- **Eliminar elementos**: `remove(x)` borra la primera ocurrencia de `x`; `pop([i])` extrae y devuelve el elemento en la posición `i`; `clear()` vacía la lista.
- **Reordenar**: `sort()` ordena la lista en su lugar; `sorted(lista)` devuelve una nueva lista ordenada; `reverse()` invierte el orden.
- **Buscar y contar**: `index(x)` devuelve la posición de la primera aparición de `x`; `count(x)` devuelve cuántas veces aparece.
- **Copiar**: `lista.copy()` o `lista[:]` devuelve una copia superficial.
- **Slicing**: `lista[inicio:fin:paso]` extrae sublistas.

### Ejemplo
```python
numeros = [10, 5, 7, 3, 8]
numeros.append(2)
numeros.insert(2, 9)
ultimo = numeros.pop()
numeros.remove(7)

ordenados = sorted(numeros)
numeros.sort(reverse=True)

primeros_tres = numeros[:3]
ultimos_dos = numeros[-2:]
saltos_de_dos = numeros[::2]
invertida = numeros[::-1]
```

## 2. Tuplas
Las tuplas (**tuple**) son secuencias inmutables: una vez creadas, no se pueden añadir ni eliminar elementos. Útiles para datos que no deben cambiar.

```python
punto = (4, 5)
x, y = punto

coordenadas = {(0, 0): "origen", (1, 2): "punto A"}
```

## 3. Conjuntos
Un conjunto (**set**) es una colección no ordenada y sin duplicados.

```python
a = {1, 2, 3}
b = set([3, 4, 5])

print(a | b)  # unión
print(a & b)  # intersección
```

## 4. Diccionarios
Almacenan pares **clave-valor**, claves únicas e inmutables.

```python
persona = {"nombre": "Ana", "edad": 25}
persona["profesion"] = "Ingeniera"
print(persona.get("correo", "sin correo"))
```

## 5. Comprensiones
Permiten construir colecciones de forma compacta y legible.

```python
impares_cuadrados = [x**2 for x in range(11) if x % 2 != 0]
vocales = {c.lower() for c in "Esto es un ejemplo" if c.lower() in 'aeiou'}
cubos = {x: x**3 for x in range(6) if x % 2 == 0 and x**3 > 20}
```

---