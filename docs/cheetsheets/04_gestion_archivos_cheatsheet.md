# 📝 Cheatsheet: Gestión de Archivos en Python

## 📂 Abrir y cerrar archivos
```python
with open('archivo.txt', 'r', encoding='utf-8') as f:
    contenido = f.read()
```

## ✍️ Modos de apertura
- r: lectura
- w: escritura (sobrescribe)
- a: añadir al final
- b: binario
- r+: lectura y escritura

## 🧹 Posicionamiento
```python
f.tell()       # posición actual
f.seek(0)      # mover cursor
```

## 🗑️ Operaciones con os
```python
import os
os.remove('archivo.txt')
os.rename('viejo.txt', 'nuevo.txt')
os.rmdir('carpeta')
```

## 📊 CSV
```python
import csv
with open('data.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for fila in reader:
        print(fila)
```

## 🌐 JSON
```python
import json
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump({"x": 1}, f, indent=4)
```

## 💡 Tip rápido
Siempre usa with para asegurar el cierre de archivos incluso si hay errores.
