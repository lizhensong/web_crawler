#!usr\bin\python3
# -*- encoding: UTF-8 -*-

__author__ = 'Wolf li'


class Field:

    def __init__(self, name, column_type, default):
        self.name = name
        self.column_type = column_type
        self.default = default

    def __str__(self):
        return '{}:{}:{}'.format(self.__class__.__name__, self.column_type, self.name)


class IntegerField(Field):

    def __init__(self, name=None, default=0):
        super().__init__(name, 'bigint', default)


class FloatField(Field):

    def __init__(self, name=None, default=0.0):
        super().__init__(name, 'real', default)


class StringField(Field):

    def __init__(self, name=None, column_type='varchar(100)', default=None):
        super().__init__(name, column_type,  default)


class BooleanField(Field):

    def __init__(self, name=None, default=False):
        super().__init__(name, 'boolean', default)


class TextField(Field):

    def __init__(self, name=None, default=None):
        super().__init__(name, 'text', default)
