import string
class Alpha:
    __slots__ = *string.ascii_lowercase

    def __init__(self, **kwargs):
        for kwarg in kwargs:
            self.kwarg = kwargs[kwarg]
        print(kwargs)

    
