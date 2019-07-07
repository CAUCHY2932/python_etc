# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/5/9 10:49
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from .models import ContactGroup, Contact


class ContactModelView(ModelView):
    datamodel = SQLAInterface(Contact)

    label_columns = {'contact_group': 'Contacts Group'}
    list_columns = ['name', 'personal_cellphone', 'birthday', 'contact_group']

    show_fieldsets = [('Summary',
                       {'fields': ['name', 'address', 'contact_group']}),
                      ('Personal Info', {'fields': ['birthday',
                                                    'personal_phone',
                                                    'personal_cellphone'],
                                         'expanded': False}),
                      ]
    search_columns = ['name', 'address']


class GroupModelView(ModelView):
    datamodel = SQLAInterface(ContactGroup)
    related_views = [ContactModelView]


# class MyView(ModelView):
#     datamodel = SQLAInterface(MyTable)
#     search_columns = ['name','address']

