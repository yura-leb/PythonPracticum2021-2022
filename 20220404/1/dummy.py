'''
Dummy module.
'''

#Just a const
DUMMY_CONST = 100


class Dummy:
    '''
    Dummy class.
    '''

    def __init__(self, val):
        '''
        Dummy init.

        :param val: Initial value
        '''
        self. value = val

    def incr(self, add):
        '''
        Increment value.

        :param add An object to add value
        '''
        self.value += add

    def __str__(self):
        '''
        Stringify me.

        :return: Stringified value
        '''
        return f"<{self.value}>"

    def str(self, sep):
        '''
        Custom str.

        :param sep: Fisrt and last string
        :return: Stringified value
        '''
        return f"{sep}{self.value}{sep}"
