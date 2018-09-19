" Settings
set numberwidth=2
set nocompatible      
set t_Co=256 
set expandtab
set autoindent
set number 
set relativenumber number
set background=dark
set backspace=indent,eol,start
set shiftwidth=4
set tabstop=4
set encoding=utf-8
set noswapfile
set incsearch
syntax on
filetype plugin on

" Global variables 
let mapleader = " "
let maplocalleader = ","
let g:airline_powerline_fonts = 1
let g:vimtex_view_method = 'zathura'
let g:vimtex_latexmk_continuous = 1
let g:vimtex_compiler_engine = 'xelatex'
let python_highlight_all = 1
let g:ycm_server_python_interpreter = '/usr/bin/python'

if empty(v:servername) && exists('*remote_startserver')
    call remote_startserver('VIM')
endif


" Mappings
nnoremap <leader>9 :w<cr>
nnoremap <leader>0 :q<cr>
nnoremap <c-c> :NERDTreeToggle<cr>
nnoremap <c-j> <esc>/<++><cr>da>i
inoremap <c-n> <esc>$a


" Vim colors
colorscheme wal

" Automatic Commands
"Keymaps
autocmd VimEnter * hi Normal ctermbg=none
autocmd BufRead,BufNewFile *.md,*.tex set tw=79
autocmd FileType tex set tw=79
autocmd FileType *.py set tw=79
autocmd FileType gitcommit set tw=72
autocmd FileType python inoremap , ,<space>
autocmd FileType tex inoremap , ,<space>
autocmd FileType tex inoremap . .<space>
autocmd FileType tex inoremap <c-a> \'
autocmd FileType tex inoremap <c-g> \`
autocmd FileType tex inoremap <c-c> \c<space>c
autocmd FileType tex inoremap <c-t> \~
autocmd FileType tex inoremap <c-f> \^
autocmd BufNewFile *.tex 0r ~/.vim/templates/skeleton.tex
autocmd BufNewFile *.sh 0r ~/.vim/templates/skeleton.sh

"Vundle Configuration
filetype off                  " required
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" Installed Plugins
Plugin 'VundleVim/Vundle.vim'
Plugin 'vim-airline/vim-airline'
Plugin 'lervag/vimtex'
Plugin 'scrooloose/nerdtree' 
Plugin 'tpope/vim-fugitive'
Plugin 'git://git.wincent.com/command-t.git'
Plugin 'rstacruz/sparkup', {'rtp': 'vim/'}
Plugin 'Valloric/YouCompleteMe'
Plugin 'davidhalter/jedi-vim'
"Plugin 'ivanov/vim-ipython'
"Plugin 'broesler/jupyter-vim'
Plugin 'python-mode/python-mode'
call vundle#end()            " required
filetype plugin indent on    " required

