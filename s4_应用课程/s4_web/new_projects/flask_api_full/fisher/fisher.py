from app import create_app
from app.models import db
from flask import session
from datetime import timedelta

__author__ = "七月"

app = create_app()

# with app.app_context():
#     db.drop_all()

# if app.config['CHECK_DB']:
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    # 如果要使用vscode调试，需要将debug设置为False，否则无法命中请求断点
    app.run(host='0.0.0.0', debug=True)


