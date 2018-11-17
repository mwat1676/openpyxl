# Copyright (c) 2010-2018 openpyxl


try:
    from abc import ABC
except ImportError:
    from abc import ABCMeta
    ABC = ABCMeta('ABC', (object, ), {})
