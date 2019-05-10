# centos7安装python3


wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-latest-Linux-x86_64.sh

sudo sh ./Miniconda3....

conda create -n jupyter


conda activate jupyter


pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ xxx

numpy pandas 


或者设置为
cat > ~/.pip/pip.conf
[global]
index-url = http://mirrors.aliyun.com/pypi/simple/
[install]
trusted-host = mirrors.aliyun.com


pip install jupyterlab

Consider using the `--user` option or check the permissions

pip install --user jupyterlab



jupyter notebook --generate-config


打开ipython
ipython
from notebook.auth import passwd
passwd()
Enter password: 123456
Verify password: 123456
‘sha1:e00ee9ab9a42:22e8c0dc771612348eeee698cde8ec77fba42e7f’
exit()


sha1:1ee6f09f898e:e352babd3864f2221d538de2b001d4db95da0e2a


    把生成的密文‘sha:xx…’复制下来
    修改默认配置文件 vi ~/.jupyter/jupyter_notebook_config.py


c.NotebookApp.ip='*'
c.NotebookApp.allow_root = True
c.NotebookApp.password = u'sha1:e00ee9ab9a42:22e8c0dc771612348eeee698cde8ec77fba42e7f'
c.NotebookApp.open_browser = False
c.NotebookApp.port =8888
c.ContentsManager.root_dir = '/data/jupyter/root'

c.NotebookApp.allow_remote_access = True

防火墙开放8888端口

    firewall-cmd --zone=public --add-port=8888/tcp --permanent
    systemctl restart firewalld.service
    iptables -L -n

启动jupyter notebook：

    nohup jupyter lab --allow-root &


登录jupyter lab

    http://服务器ip地址:8888/lab


10.10.10.100:8888/lab