def classdec(cls):
    class Newcl(cls):
        def __str__(self):
            res = super().__str__()
            return f'>>>{res}<<<'
    return Newcl

@classdec
class A(str):
    pass

