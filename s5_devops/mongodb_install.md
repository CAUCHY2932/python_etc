# 在centos7上安装mongodb

## 添加源

>  vim /etc/yum.repos.d/MongoDB.repo

    [mongodb-org-3.6]

    name=MongoDB Repository

    baseurl=https://repo.mongodb.org/yum/redhat/\$releasever/mongodb-org/3.6/x86_64/

    gpgcheck=1

    enabled=1

    gpgkey=https://www.mongodb.org/static/pgp/server-3.6.asc


> yum -y install mongodb-org


---> Package mongodb-org.x86_64 0:3.6.11-1.el7 will be installed
--> Processing Dependency: mongodb-org-tools = 3.6.11 for package: mongodb-org-3.6.11-1.el7.x86_64
--> Processing Dependency: mongodb-org-shell = 3.6.11 for package: mongodb-org-3.6.11-1.el7.x86_64
--> Processing Dependency: mongodb-org-server = 3.6.11 for package: mongodb-org-3.6.11-1.el7.x86_64
--> Processing Dependency: mongodb-org-mongos = 3.6.11 for package: mongodb-org-3.6.11-1.el7.x86_64
--> Running transaction check


太慢可以使用清华rpm安装



# 在ubuntu上安装mongodb



# 在windows上安装mongodb


