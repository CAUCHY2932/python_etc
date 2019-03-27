# vim settings
> author:young
## change dir to current usr profile

```
$ cd ~
```

## edit the vimrc file

```
$ vim ~/.vimrc
```

## set the file

```
set ts=4
set expandtab
set autoindent
set number


```
## 在vim编辑器python实现tab补全功能

### 第一步:安装配置pydiction
```
$ wget https://github.com/rkulla/pydiction/archive/master.zip

$ unzip master.zip

$ mv pydiction-master pydiction

$ mkdir -p ~/.vim/tools/pydiction

$ cp -r pydiction/after ~/.vim

$ cp pydiction/complete-dict ~/.vim/tools/pydiction

```
确保文件结构如下
```
$ tree ~/.vim

/root/.vim

├── after

│ └── ftplugin

│ └── python_pydiction.vim

└── tools

└── pydiction

└── complete-dict

```
### 第二步:创建~/.vimrc,确保其中内容如下
```
$ vim ~/.vimrc

filetype plugin on

let g:pydiction_location = '~/.vim/tools/pydiction/complete-dict'
```
### 第三步:用vim编辑一个py文件，再输入函数时按tab补全





 另外，Python编程是靠缩进来规定语法的，当你使用vim写python时，要注意tab与空格的区别。一般我们写Python都是以4个空格表缩进标准的，所以在代码中不要把空格与tab混用（两者ASCII码是不同的），要不一直用空格，要不就一直用tab，不然会导致程序报错。推荐把vim的tab变为4个空格，增加编程效率。

 " 设置Tab键的宽度[等同的空格个数]

 set tabstop=4

 " 每一次缩进对应的空格数

 set shiftwidth=4

 " 按退格键时可以一次删掉4个空格

 set softtabstop=4

 在root用户家目录下的.vimrc中设置，对所有用户生效
 
## setting python-mode ide


### install pathogen


```
mkdir -p ~/.vim/autoload ~/.vim/bundle

curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim

```


vim ~/.vimrc
put the content in vimrc file

```
execute pathogen#infect()
syntax on
filetype plugin indent on

```

### put python-mode module in ~/.vim.bundle

cd ~/.vim/bundle

git clone https://github.com/klen/python-mode.git

### in vim file rebuild helptags
:helptags

```
:help filetype-plugin-on
:help filetype-indent-on


```

