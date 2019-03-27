# -*- coding=utf-8 -*-
"""
    2019/3/11 20:36
    author:young
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello world!'


if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=8091, debug=True) # default 0.0.0.0 cannot be listen!
    app.run(port=8091, debug=True)
