yum -y install cyrus-sasl cyrus-sasl-devel cyrus-sasl-lib
yum install gcc-c++


pip install sasl -i https://pypi.douban.com/simple
pip install numpy -i https://pypi.douban.com/simple
pip install pandas==0.23.4 -i https://pypi.douban.com/simple





pip install superset -i https://pypi.douban.com/simple

pip install sqlalchemy==1.2.18 -i https://pypi.douban.com/simple

# Create an admin user (you will be prompted to set a username, first and last name before setting a password)
fabmanager create-admin --app superset
 
# Initialize the database
superset db upgrade
 
# 加载superset例子，可要可不要
superset load_examples
 
# Create default roles and permissions
superset init
 
# To start a development web server on port 8088, use -p to bind to another port
superset runserver -d
