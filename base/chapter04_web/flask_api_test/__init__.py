from flask.blueprint import Blueprint


web = Blueprint('web')

@web.route('/index')
def index():
    return 0


