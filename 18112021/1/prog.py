def decclass(clas):
    def __init__(self, *args):
        num += 1
        clas.__init__(*args)

    def __del__(self):
        num -= 1
        clas.__del__()

    

    return clas
