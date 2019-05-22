import os

flask_pro = input('请输入你要创建的flask工程名：\n')

os.mkdir('./{}'.format(flask_pro))

os.mkdir('./{}/app'.format(flask_pro))
# 创建admin目录
os.mkdir('./{}/app/admin'.format(flask_pro))
# 创建home目录
os.mkdir('./{}/app/home'.format(flask_pro))
# 创建static目录
os.mkdir('./{}/app/static'.format(flask_pro))
# 创建templates目录
os.mkdir('./{}/app/templates'.format(flask_pro))

# 创建templates目录下的home
os.mkdir('./{}/app/templates/home'.format(flask_pro))
# 创建templates目录下的admin
os.mkdir('./{}/app/templates/admin'.format(flask_pro))


os.mknod('./{}/app/admin/__init__.py'.format(flask_pro))

os.mknod('./{}/app/admin/forms.py'.format(flask_pro))

os.mknod('./{}/app/admin/views.py'.format(flask_pro))

os.mknod('./{}/app/home/__init__.py'.format(flask_pro))

os.mknod('./{}/app/home/forms.py'.format(flask_pro))

os.mknod('./{}/app/home/views.py'.format(flask_pro))


os.mknod('./{}/app/__init__.py'.format(flask_pro))

os.mknod('./{}/app/models.py'.format(flask_pro))


os.mknod('./{}/manage.py'.format(flask_pro))
