# coding:utf-8

from flask import Flask
from test_server.models import Person
from test_server.extensions import db
import os, time


basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
 
app = Flask(__name__)
 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:////' + os.path.join(basedir, 'data.db')
app.config["DEBUG"] = True
db.init_app(app)
 
 
def read_data():
    with open("fake_data", "r") as f:
        data = f.readlines()
    return data
 
 
def test_bulk_save_objects(data):
    start = time.time()
    db.session.bulk_save_objects([Person(name=i) for i in data])
    db.session.commit()
    print(time.time() - start)
    


def test_bulk_insert_mappings(data):
    start = time.time()
    db.session.bulk_insert_mappings(
        Person,
        [dict(name=i) for i in data]
    )
    db.session.commit()
    print(time.time() - start)
    
 
 
def test_engine_execute(data):
    start = time.time()
    db.engine.execute(
        Person.__table__.insert(),
        [dict(name=i) for i in data]
    )
    print(time.time() - start)




@app.route("/index", methods=["GET"])
def index():
    data = read_data()
    data = map(lambda i: i.strip(), data)
    test_bulk_save_objects(data)# 2.1244254112243652秒
    test_bulk_insert_mappings(data)# 0.7736368179321289秒
    test_engine_execute(data)#0.3461315631866455秒
    return 'ok'
 
 
if __name__ == '__main__':
    app.run()
# 通过10万条数据的插入可以对比

# 使用engine.execute的速度是最快的，比较接近原生sql

# 使用insert_mappings的速度接近engine.execute

# 使用save_objects就非常慢了，因为他要把数据转化成对象再插入数据

# 而前两种使用字典作为数据映射所以非常的快
