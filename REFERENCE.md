# Scripts Reference

## .vimrc

```vimrc
" Cargar configuraciones modulares
source ~/.vim/configs/general.vim
source ~/.vim/configs/keybindings.vim
source ~/.vim/configs/functions.vim
source ~/.vim/configs/settings.vim
```
## general.vim

```vim
syntax on
filetype on
set backspace=indent,eol,start
set clipboard=unnamedplus
set autowrite
set mouse=a
colorscheme habamax
```
## settings.vim

```vim
set number
set relativenumber
set tabstop=2
set expandtab
set shiftwidth=2
set softtabstop=2
set autoindent
set smartindent
set expandtab
set cindent
set scrolloff=8
set sidescrolloff=8
set wildmenu
set completeopt=menu,menuone,noselect
```
## keybindings.vim

```vim
" Leader Key
let mapleader = " "

" Basic Keybindings
nnoremap <Leader>w :w<CR>
nnoremap <Leader>wq :wq<CR>
nnoremap <Leader>q :q<CR>
nnoremap <Leader>wr <C-w>r
nnoremap <Leader>bn :bnext<CR>

" Navigation
inoremap <C-h> <Left>
inoremap <C-l> <Right>
inoremap <C-j> <Down>
inoremap <C-k> <Up>

" Window Navigation
nnoremap <Leader>k :wincmd +<CR>
nnoremap <Leader>j :wincmd -<CR>
nnoremap <Leader>l :wincmd ><CR>
nnoremap <Leader>h :wincmd <<CR>
nnoremap <C-j> <C-W>j
nnoremap <C-k> <C-W>k
nnoremap <C-l> <C-W>l
nnoremap <C-h> <C-W>h
```
## functions.vim

```vim
" Function for Compilation
function! Compile()
  execute "w"
  silent execute "!g++ % -o runfiles/executable > runfiles/problem.log 2>&1 && echo 'Compilacion exitosa :3' >> runfiles/problem.log"
  redraw!
endfunction

" Function for Execution
function! Execute()
  silent execute "!./runfiles/executable < runfiles/data.in > runfiles/problem.out"
  if v:shell_error == 0
    silent execute "!echo 'Ejecución completa:' > runfiles/problem.log"
    silent execute "!/usr/bin/time -o runfiles/problem.log -f \"> Time: \\%S s\\n> Memory: \\%M KB\" ./runfiles/executable < runfiles/data.in > /dev/null"
  else
    silent execute "!echo 'Error en la ejecución' > runfiles/problem.log"
  endif
  redraw!
endfunction

nnoremap <Leader>cc :call Compile()<CR>
nnoremap <Leader>ce :call Execute()<CR>
nnoremap <F5> <Leader>cc
nnoremap <F6> <Leader>ce
nmap <Leader>cr <Leader>cc<CR><Leader>ce
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

