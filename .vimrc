" Settings
set numberwidth=2
set nocompatible      
set t_Co=256 
set expandtab
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
let maplocalleader = ";"
let g:airline_powerline_fonts = 1
let g:vimtex_view_method = 'zathura'
let g:vimtex_latexmk_continuous = 1

if empty(v:servername) && exists('*remote_startserver')
    call remote_startserver('VIM')
endif


" Mappings
nnoremap ;k :m.-2<cr>
nnoremap ;j :m.+1<cr>
nnoremap <leader>9 :w<cr>
nnoremap <leader>0 :q<cr>
nnoremap <c-c> :NERDTreeToggle<cr>

" Vim colors
colorscheme wal

" Automatic Commands
"Keymaps
autocmd VimEnter * hi Normal ctermbg=none
autocmd BufRead,BufNewFile *.md,*.tex set tw=79
autocmd FileType gitcommit set tw=72
autocmd FileType tex inoremap <c-a> \'
autocmd FileType tex inoremap <c-g> \`
autocmd FileType tex inoremap <c-c> \c<space>
autocmd FileType tex inoremap <c-t> \~
autocmd FileType tex inoremap <c-f> \^


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
call vundle#end()            " required
filetype plugin indent on    " required

