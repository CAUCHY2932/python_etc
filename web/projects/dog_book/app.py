from datetime import datetime
from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired


app = Flask(__name__)


bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'hard to guess'


class NameForm(FlaskForm):
    name = StringField('what\'s your name', validators=[DataRequired()])
    submit = SubmitField('submit')
    pass


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', current_time=datetime.utcnow(), form=form, name=name)


@app.route('/index')
def index2():
    user_agent = request.headers.get('User-Agent')
    return '<p>your browser is {}</p>'.format(user_agent)


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500






if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
