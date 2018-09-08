# coding:utf-8
class Foo(object):
    """属性的查找顺序，getattr方法"""
    def __init__(self):
        pass

    def __getattr__(self, item):
        print item,
        return self

    def __str__(self):
        return ""


print (Foo().think.different.junxin)
