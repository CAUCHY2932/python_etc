# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/5/6 17:27
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
from flask import Flask, render_template, request, url_for
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *

app = Flask(__name__)
Bootstrap(app)
nav = Nav()
nav.register_element('top', Navbar(u'Flask入门',
                                    View(u'主页', 'home'),
                                    View(u'关于', 'about'),
                                    Subgroup(u'项目',
                                             View(u'项目一', 'about'),
                                             Separator(),
                                             View(u'项目二', 'service'),
                                             ),
                                    ))

nav.init_app(app)


@app.route('/')
def home():
    return render_template('home.html', title_name='welcome')


@app.route('/service')
def service():
    return 'service'


@app.route('/about')
def about():
    return 'about'


if __name__ == '__main__':
    app.run(debug=True)
