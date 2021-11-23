import string
class Alpha:
    __slots__ = list(string.ascii_lowercase)

    def __init__(self, **kwargs):
        for kwarg in kwargs:
            self.__setattr__(kwarg, kwargs[kwarg])
                
    def __str__(self):
        res = ''
        for i in range(len(self.__slots__)):
            try:
                res += self.__slots__[i] + ': ' + str(self.__getattribute__(self.__slots__[i])) + ', '
            except:
                pass
        return res[:-2]

class AlphaQ:
    def __init__(self, **kwargs):
        for kwarg in kwargs:
            self.__setattr__(kwarg, kwargs[kwarg])
        
    def __str__(self):
        res = ''
        for name in sorted(self.__dict__):
            res += name + ': ' + str(self.__getattr__(name)) + ', '
        return res[:-2]

    def __getattr__(self, name):
        try:
            return self.__dict__[name]
        except KeyError:
            raise AttributeError

import sys
exec(sys.stdin.read())
