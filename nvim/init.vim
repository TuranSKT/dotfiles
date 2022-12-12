call plug#begin()

" Display indents
Plug 'yggdroot/indentline'

" Python auto completion engine
Plug 'davidhalter/jedi-vim'

" Highlight indicator
Plug 'machakann/vim-highlightedyank'

" Colorscheme
Plug 'joshdick/onedark.vim'

call plug#end()

syntax on

set expandtab
set smartindent
set nu
set nowrap
set smartcase
set noswapfile
set nobackup
set undodir=~/.config/nvim/undodir
set undofile
set incsearch

set splitright
set splitbelow

" Remove the duplicate --INSERT-- information
set noshowmode

" Add folding shortcuts and settings
set foldmethod=indent
set foldnestmax=10
set nofoldenable
set foldlevel=99
set signcolumn=no

" indentline configs
let g:indentLine_enabled = 1
let g:indentLine_char_list = ['|', '¦', '┆', '┊']
let g:indentLine_setColors = 1
let g:indentLine_color_gui = "#5C6370"
let g:indentLine_showFirstIndentLevel = 1

let &t_8f = "\<Esc>[38;2;%lu;%lu;%lum"
let &t_8b = "\<Esc>[48;2;%lu;%lu;%lum"

"set background=dark
colorscheme onedark
set t_Co=256

" Python configuration, Highlight self
augroup python
    autocmd!
    autocmd FileType python
                \   syn keyword pythonSelf self
                \   | highlight def link pythonSelf Special
augroup end

"Use 24-bit (true-color) mode in Vim/Neovim when outside tmux.
"If you're using tmux version 2.2 or later, you can remove the outermost $TMUX check and use tmux's 24-bit color support
"(see < http://sunaku.github.io/tmux-24bit-color.html#usage > for more information.)
if (empty($TMUX))
  if (has("nvim"))
    "For Neovim 0.1.3 and 0.1.4 < https://github.com/neovim/neovim/pull/2198 >
    let $NVIM_TUI_ENABLE_TRUE_COLOR=1
  endif
  "For Neovim > 0.1.5 and Vim > patch 7.4.1799 < https://github.com/vim/vim/commit/61be73bb0f965a895bfb064ea3e55476ac175162 >
  "Based on Vim patch 7.4.1770 (`guicolors` option) < https://github.com/vim/vim/commit/8a633e3427b47286869aa4b96f2bfc1fe65b25cd >
  " < https://github.com/neovim/neovim/wiki/Following-HEAD#20160511 >
  if (has("termguicolors"))
    set termguicolors
  endif
endif
