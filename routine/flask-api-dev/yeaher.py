# -*- coding:utf-8 -*-


from flask import Flask
from app.v1.web import web
print(web)
app = Flask(__name__)
app.register_blueprint(web, url_prefix='/testweb')
@app.route("/")
def index():
	return "hello world"

if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0", port=8091)
