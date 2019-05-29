#!usr\bin\python3
# -*- encoding:utf-8 -*-

__author__ = 'wolf li'

import pickle


def save(data, path):
    with open(path, 'wb') as f:
        pickle.dump(data, f)


def read(path):
    with open(path, 'rb') as f:
        return pickle.load(f)
