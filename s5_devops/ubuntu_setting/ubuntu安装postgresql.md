## ubuntu 安装postgresql





sudo apt-get update

sudo apt-get install postgresql postgresql-client

## 创建超级用户

sudo -i -u postgres

## 进入命令行

```bash
~$ psql
psql (9.5.17)
Type "help" for help.

postgres=# 
```

输入以下命令退出 PostgreSQL 提示符：

```bash
\q
```

PostgreSQL 安装完成后默认是已经启动的，但是也可以通过下面的方式来手动启动服务。

```bash
sudo /etc/init.d/postgresql start   # 开启
sudo /etc/init.d/postgresql stop    # 关闭
sudo /etc/init.d/postgresql restart # 重启
```

## 配置远程访问

find / -name postgresql.conf 

末尾加上 listen_addresses = '*'

启用密码验证

#password_encryption = on 改为 password_encryption = on

修改pg_hba.conf文件的内容

可访问的用户ip段

在文件末尾加入:

host all all 0.0.0.0/0 md5

重启postgresql

service postgresql restart

## 密码配置

### 修改默认用户postgres的密码

#### 登录postgresql

sudo -i -u postgres 

psql

#### 修改密码


ALTER USER postgres WITH PASSWORD  'postgres';

**注：**

- 密码postgres要用引号引起来
- 命令最后有分号

### 开启数据库端口

sudo ufw allow 5432

sudo ufw reload

sudo service postgresql restart

### 查看当前数据库状态

sudo service postgresql status



### 修改linux系统postgres用户的密码

#### 删除用户postgres的密码

sudo passwd -d postgres

#### 设置用户postgres的密码

sudo -u postgres passwd

