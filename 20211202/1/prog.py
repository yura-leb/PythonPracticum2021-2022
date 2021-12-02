def decor(fun):
    def newfun(*args, **kwargs):
        print(fun.__name__(), *args, **kwargs)
        return fun(*args, **kwargs)
    return newfun

class dump(type):
##    def __call__(self, *args, **kwargs):
##        print("call", self, args, kwargs)
##        return super().__call__(*args, **kwargs)
##
##    def __new__(cls, name, parents, ns):
##        print("new", cls, name, parents, ns)
##        return super().__new__(cls, name, parents, ns)

    def __init__(self, name, parents, ns):
        print("__init__: ", ns)
        for fun in ns:
            fun = decor(fun) ##исправить
        return super().__init__(name, parents, ns)
    
