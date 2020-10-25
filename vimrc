" 编辑相关 =================================
" 展开tab
set expandtab
" tab宽度
set tabstop=4
set softtabstop=4
" 自动缩进
set autoindent
set shiftwidth=4
set smartindent

" 编码 =======================================
set fileencodings=utf-8,gbk

" 外观相关 =================================
" 256色模式
set t_Co=256
set term=xterm-256color
" 主题
colorscheme desert
" 注释设置成淡灰色
highlight Comment ctermfg=202
highlight PreProc ctermfg=82
" 高亮搜索的词
set hlsearch
" 显示所有字符
set list
set listchars=eol:$,tab:~~,trail:.,nbsp:.,precedes:^,extends:^
highlight NonText ctermfg=239
highlight SpecialKey ctermfg=239
" 显示行号
set number
" 语法高亮 
syntax on

