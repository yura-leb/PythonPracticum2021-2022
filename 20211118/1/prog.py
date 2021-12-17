def objcount(cls):
    class newcls(cls):
        counter = 0
        def __init__(self, *args, **kwargs):
            newcls.counter += 1
            try:
                super().__init__(*args, **kwargs)
            except:
                super().__init__()

        def __del__(self):
            newcls.counter -= 1
            try:
                super().__del__()
            except Exception:
                pass
    return newcls

import sys
exec(sys.stdin.read())
