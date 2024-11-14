# Scripts Reference

## Hola_mundo_2.py

> **COMENTARIOS**
>
> La tercera es la vencida xd aqui vamos
>
> Ejemplo de dejar aqui los comentarios para la descripcion de la reference

```python
#!/usr/bin/env python3


print("hola gente :D")
```
## layouts.vim

```vim
" Se usa como: vim A-Problem.cpp -S layouts.vim
set splitright
vs runfiles/data.in
set splitbelow
sp runfiles/judge.out
sp runfiles/problem.out
set autoread
sp runfiles/problem.log
set autoread
wincmd h
```
> **Recursos adicionales en dir: vim-layouts**

*B-Problem.cpp*

```cpp
#include<iostream>

using namespace std;

int main(){
  cout << "Hellooo";
}

```

*A-Problem.cpp*

```cpp
#include<iostream>

using namespace std;

int main(){
  string str;
  getline(cin, str);
  cout << "Esta es la salida del codigo\n";
  cout << "Data.in: " << str;
}

```

> **Recursos adicionales en dir: runfiles**

*problem.out*

```out
Esta es la salida del codigo
Data.in: Aqui deberian ir los datos de entrada
```

*data.in*

```in
Aqui deberian ir los datos de entrada

```

*judge.out*

```out
Aqui deberia ir la salida esperada

```

*problem.log*

```log
> Time: 0.00 s
> Memory: 3704 KB

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
## hola_mundo.sh

```sh
#!/usr/bin/env zsh

echo "Hola mundo"
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
> **Recursos adicionales en dir: resources**

*hola_mundo.txt*

```txt
Hola mundo desde un archivo :>

```

