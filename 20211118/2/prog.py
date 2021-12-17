class Num:
    def __get__(self, obj, cls):
        try:
            return obj._val
        except:
            return 0

    def __set__(self, obj, value):
        if hasattr(value, 'real'):
            obj._val = value
        else:
            obj._val = len(list(value))

    def __delete__(self,obj):
        obj._val = 0

import sys
exec(sys.stdin.read())


