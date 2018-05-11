# -*- coding: utf-8 -*-

"""Various utility functions."""


def strclass(cls):
    return "%s.%s" % (cls.__module__, cls.__name__)