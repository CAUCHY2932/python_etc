# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/5/9 10:56
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
from app import appbuilder
from app.model_views import GroupModelView, ContactModelView

appbuilder.add_view(
    GroupModelView,
    "List Groups",
    icon="fa-folder-open-o",
    category="Contacts",
    category_icon="fa-envelope"
)
appbuilder.add_view(
    ContactModelView,
    "List Contacts",
    icon="fa-envelope",
    category="Contacts"
)
