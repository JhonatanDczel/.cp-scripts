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
