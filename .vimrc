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


" Mappings
nnoremap ;k :m.-2<cr>
nnoremap ;j :m.+1<cr>
nnoremap <leader>s :w<cr>
nnoremap <leader>0 :q<cr>
nnoremap <c-c> :NERDTreeToggle<cr>

" Vim colors
colorscheme wal

" Automatic Commands
"Keymaps
autocmd VimEnter * hi Normal ctermbg=none


"Vundle Configuration
filetype off                  " required
set rtp+=/home/hugoweslien/.vim/bundle/Vundle.vim
call vundle#begin()

" Installed Plugins
Plugin 'VundleVim/Vundle.vim'
Plugin 'Shougo/deoplete.nvim'
let g:deoplete#enable_at_startup = 1
let g:python_host_prog = '/usr/bin/python'
let g:python3_host_prog = '/usr/bin/python3'
Plugin 'roxma/nvim-yarp'
Plugin 'roxma/vim-hug-neovim-rpc'
Plugin 'zchee/deoplete-jedi'
Plugin 'carlitux/deoplete-ternjs', { 'do' : 'npm install -g tern' }
Plugin 'ternjs/tern_for_vim'
Plugin 'vim-airline/vim-airline'
let g:airline_powerline_fonts = 1
Plugin 'xuhdev/vim-latex-live-preview'
Plugin 'sheerun/vim-polyglot'
Plugin 'mxw/vim-jsx'
Plugin 'pangloss/vim-javascript'
Plugin 'nsf/gocode', { 'rtp' : 'vim/' }
Plugin 'elzr/vim-json'
Plugin 'LateX-Box-Team/LateX-Box'
Plugin 'godlygeek/tabular'
Plugin 'plasticboy/vim-markdown'
Plugin 'scrooloose/nerdtree' 
Plugin 'fatih/vim-go', { 'do' : ':GoInstallBinaries' }
Plugin 'vim-python/python-syntax'
let g:python_highlight_all = 1
Plugin 'tpope/vim-surround' 
Plugin 'tpope/vim-fugitive'
Plugin 'dylanaraps/wal.vim'
Plugin 'git://git.wincent.com/command-t.git'
"Plugin 'file:///home/gmarik/path/to/plugin'
Plugin 'rstacruz/sparkup', {'rtp': 'vim/'}
call vundle#end()            " required
filetype plugin indent on    " required

