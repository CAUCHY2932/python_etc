# -*- coding:utf-8 -*-
"""
create by young on 2018-12-31 22:32 
"""

__author__ = 'young'


class Redprint:
    def __init__(self, name):
        self.name=name
        self.mound=[]
        pass

    def route(self, rule, **options):
        def decorator(f):
            self.mound.append((f, rule, options))
            # endpoint=options.pop()
            return f
        return decorator


    def register(self,bp, url_prefix=None):
        if url_prefix is None:
            url_prefix="/"+self.__name__
        for f, rule, options in self.mound:
            endpoint=options.pop('endpoint',f.__name__)
            bp.add_url_rule(url_prefix+rule, endpoint, f, **options)







