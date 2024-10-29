# Guidelines

> [!IMPORTANT]
> SOLO FUNCIONA EN SISTEMAS UNIX

- Para scripts en otros lenguajes, incluye en la primera linea el shebang (`#!`) referenciando el interprete
- Los scripts van en la carpeta `scripts` xd, si quieres agregar un script, crea un nuevo directorio con el nombre de tu script
- Para evitar conflictos entre los nombres de los comandos, todos los comandos finales iniciaran con un `cps-`
  - **Ejemplo**: `compile_exercise.sh` sera llevado a `/bin` como: `cps-compile_exercise`
- Si necesitas hacer que tu script use algun archivo, incluyelos dentro de la carpeta que contiene a tu script, si es un recurso compartido deberías incluirlo en un directorio en `/resources`
- Para referenciar a algun archivo, usa siempre una ruta relativa al directorio home
  - **Ejemplo:** Para referenciar `template-1.cpp` -> `~/.cp-scripts/public/tempate-1.cpp`
