import types
def decor(fun, *args, **kwargs):
    def newfun(*args, **kwargs):
        print(args[1:], kwargs)
        return fun(*args, **kwargs)
    return newfun

class dump(type):
    def __new__(cls, name, parents, ns):
        for name, value in ns.items():
            if callable(value):
                ns[name] = decor(value)
        return super(dump, cls).__new__(cls, name, parents, ns)
           
import sys
exec(sys.stdin.read())
