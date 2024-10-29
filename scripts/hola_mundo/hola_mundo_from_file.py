#!/usr/bin/env python3
import os

home_directory = os.path.expanduser("~")

file_path = os.path.join(
    home_directory, ".cp-scripts/scripts/hola_mundo/resources/hola_mundo.txt"
)
with open(file_path, "r") as f:
    print(f.read())
