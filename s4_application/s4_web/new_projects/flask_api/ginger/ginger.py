# -*-encoding:utf-8 -*-
"""
    2019/4/20 4:10
    create by young
"""
from app.app import create_app

app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
