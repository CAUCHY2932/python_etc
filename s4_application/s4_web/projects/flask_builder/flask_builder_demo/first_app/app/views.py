from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi, has_access

from . import appbuilder, db

"""
    Create your Model based REST API::

    class MyModelApi(ModelRestApi):
        datamodel = SQLAInterface(MyModel)

    appbuilder.add_api(MyModelApi)


    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(
        MyModelView,
        "My View",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    )
"""

"""
    Application wide 404 error handler
"""
from flask_appbuilder import AppBuilder, expose, BaseView
from app import appbuilder


class MyView(BaseView):

    default_view = 'method1'

    @expose('/method1/')
    @has_access
    def method1(self):
        # do something with param1
        # and return to previous page or index
        return 'Hello'

    @expose('/method2/<string:param1>')
    @has_access
    def method2(self, param1):
        # do something with param1
        # and render template with param
        param1 = 'Goodbye %s' % (param1)
        return param1


appbuilder.add_view(MyView, "Method1", category='My View')
appbuilder.add_link("Method2", href='/myview/method2/john', category='My View')


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )


db.create_all()
