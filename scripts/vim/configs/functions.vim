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
