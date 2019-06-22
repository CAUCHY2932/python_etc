# coding:utf-8


from api import create_app


app = create_app()


@app.route('/')
def home():
    return '<h1>welcome!</h1>'


# config settings
app.config['SECRET_KEY'] = 'HARD TO GUESS'
app.config['WTF_CSRF_ENABLED'] = False
app.config['WTF_CSRF_SECRET_KEY'] = 'a random string'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + 'dev.sqlite'

# WTF_CSRF_ENABLED = False
# WTF_CSRF_SECRET_KEY = 'a random string'


if __name__ == '__main__':
    app.run(debug=True)
