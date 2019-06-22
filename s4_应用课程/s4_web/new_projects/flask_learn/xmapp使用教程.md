# xmapp

默认安装的mysql可能和phpstudy冲突
建议停止phpstudy的服务
并删除phpstudy的目录

利用phpadmin登录mysql，并修改登录需要密码

然后我们需要进入xampp安装目录下的phpMyAdmin目录，
找到config.inc.php文件

config改为cookie

$cfg['Servers'][$i]['auth_type'] = 'cookie'