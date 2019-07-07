# pipenv 的使用

pip install pipenv

pipenv graph
显示依赖

pipenv shell
进入当前目录的虚拟环境（pipfile，和pipfile.lock所在的目录），如果没有则自动创建虚拟环境

pipenv install xxx
进入虚拟环境后安装库

pipenv uninstall xxx
卸载库

exit
退出虚拟环境

