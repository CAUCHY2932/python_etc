导出转储MongoDB数据要在MongoDB中创建数据库备份，应该使用 mongodump 命令。 此命令将导出转储服务器的整个数据到转储目录。有许多选项可用于限制数据量或创建远程服务器的备份。
语法
mongodump命令的基本语法如下：
> mongodump原文出自【易百教程】，商业转载请联系作者获得授权，非商业请保留原文链接：https://www.yiibai.com/mongodb/mongodb_create_backup.html

以下是可用于 mongodump 命令的可用选项的列表。



语法
描述
示例




mongodump —host HOST_NAME —port PORT_NUMBER
此命令将备份指定的 mongod 实例的所有数据库。
mongodump --host 127.0.0.1 --port 27017


mongodump —out BACKUP_DIRECTORY
此命令将仅在指定路径上备份数据库。
mongodump --out /home/yiibai/mongobak


mongodump —collection COLLECTION —db DB_NAME
此命令将仅备份指定数据库的指定集合。
mongodump --collection mycol --db test



恢复数据要恢复备份数据，使用MongoDB的 mongorestore 命令。 此命令从备份目录中恢复所有数据。
语法
mongorestore命令的基本语法是 -
> mongorestore
Shell
在恢复数据之前，先删除当前数据库的部分数据，以演示导入恢复数据后可以查询到备份时的数据。
> db.mycol.remove({})
WriteResult({ "nRemoved" : 4 })
>
> db.mycol.find({})
>
>原文出自【易百教程】，商业转载请联系作者获得授权，非商业请保留原文链接：https://www.yiibai.com/mongodb/mongodb_create_backup.html

