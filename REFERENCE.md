# Scripts Reference

## hola_mundo.sh

```sh
#!/usr/bin/env zsh

echo "Hola mundo"
```

## hola_mundo.py

> **COMENTARIOS**
>
> Imprime hola mundo xd
>
> Esta es la descripcion del script

```python
#!/usr/bin/env python3

print("Hola mundo")
```

## hola_mundo_from_file.py

> **COMENTARIOS**
>
> Escribe hola mundo por consola xd
>
> Lee el hola mundo desde un archivo
>
> Para leer el archivo se hace uso de una ruta absoluta:
>
> "~/.cp-scripts/scripts/hola_mundo/resources/hola_mundo.txt"

```python
#!/usr/bin/env python3


import os

home_directory = os.path.expanduser("~")

file_path = os.path.join(
    home_directory, ".cp-scripts/scripts/hola_mundo/resources/hola_mundo.txt"
)

# Este comentario deberia ser parte del codigo y no de los comentarios
with open(file_path, "r") as f:
    print(f.read())
```

