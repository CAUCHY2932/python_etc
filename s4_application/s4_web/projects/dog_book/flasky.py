# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019-05-05 00:06
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
from app import create_app, db
from flask_migrate import Migrate
from app.models import User, Role
import os


app = create_app(os.environ.get('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(User=User, Role=Role, db=db)


@app.cli.command()
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
