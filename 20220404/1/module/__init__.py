'''
Dummy module.
'''

DUMMY_CONST = 100

class Dummy:
    '''
    Dummy class.
    '''

    def __init__(self, val):
        '''
        Dummy init.
        '''
        self. value = val

    def incr(self, add):
        '''
        Increment value.
        '''
        self.value += add

    def __str__(self):
        '''
        Stringify me.
        '''
        return f"<{self.value}>"

    def str(self, sep):
        '''
        Custom str.
        '''
        return f"{sep}{self.value}{sep}"
