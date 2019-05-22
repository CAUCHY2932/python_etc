https://mirrors.tuna.tsinghua.edu.cn/help/mongodb/

mongodb安装镜像帮助


新建 /etc/yum.repos.d/mongodb.repo，内容为

    [mongodb-org]
    name=MongoDB Repository
    baseurl=https://mirrors.tuna.tsinghua.edu.cn/mongodb/yum/el$releasever/
    gpgcheck=0
    enabled=1

刷新缓存并安装 mongodb-org 即可。

    sudo yum makecache
    sudo yum install mongodb-org

安装完之后记得清理repo文件

cd /etc/yum.repos.d/
rm -rf mongodb.repo


后处理

whereis mongod

vim /etc/mongod.conf
修改端口

port


启动mongodb
systemctl start mongod.service

停止mongodb
systemctl stop mongod.service

systemctl status mongod.service

新建管理员用户
mongo
use admin
db.createUser({user:"userAdmin",pwd:"123456",roles:[{role:"userAdminAnyDatabase",db:"admin"}]})

db.auth("userAdmin","123456")

新建普通用户
use test

db.createUser({user:"test",pwd:"123456",roles:[{role:"readWrite",db:"test"}]})

exit