# coding:utf-8

"""
create by young on 20190414

"""


from app import create_app

app = create_app()


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], port=1234)
