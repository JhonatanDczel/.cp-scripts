#!/usr/bin/env python3

# > Escribe hola mundo por consola xd
# > Lee el hola mundo desde un archivo
# > Para leer el archivo se hace uso de una ruta absoluta:
# > "~/.cp-scripts/scripts/hola_mundo/resources/hola_mundo.txt"

import os

home_directory = os.path.expanduser("~")

file_path = os.path.join(
    home_directory, ".cp-scripts/scripts/hola_mundo/resources/hola_mundo.txt"
)

# Este comentario deberia ser parte del codigo y no de los comentarios
with open(file_path, "r") as f:
    print(f.read())
