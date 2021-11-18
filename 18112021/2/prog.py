class Num:
    def __get__(self, obj, cls):
        try:
            return obj._val
        except:
            obj._val = 0
        return obj._val

    def __set__(self, obj, value):
        try:
            obj._val = value.real
            return
        except AttributeError:
            pass
        try:
            obj._val = len(value)
            return
        except TypeError:
            pass
        return

    def __delete__(self,obj):
        obj._val = 0

