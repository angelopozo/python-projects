# 📂 Gestión de Archivos en Python

## 🎯 Objetivos
- Abrir, cerrar, leer y escribir archivos de forma segura.
- Diferenciar modos de apertura (`r`, `w`, `a`, `b`).
- Usar `with` para cierre automático.
- Manipular archivos y carpetas con `os` y `shutil`.
- Trabajar con formatos TXT, CSV y JSON.

### Ejemplo básico
```python
with open('datos.txt', 'w', encoding='utf-8') as f:
    f.write('Primera línea\n')
```

---