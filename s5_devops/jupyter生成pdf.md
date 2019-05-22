# jupyter 输出文档

安装tex工具

https://nbconvert.readthedocs.io/en/latest/install.html#installing-tex

## 生成html
jupyter nbconvert notebook.ipynb


## 生成pdf

jupyter nbconvert --to latex 1-Redcard-Dataset.ipynb
xelatex 1-Redcard-Dataset.tex

或者

jupyter nbconvert notebook.ipynb --to pdf