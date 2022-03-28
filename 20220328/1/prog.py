import sys


class check(type):

    def __new__(cls, name, parents, ns):
        def check_annotations(self):
            if not hasattr(self, '__annotations__'):
                return True
            try:
                for name, value in self.__annotations__.items():
                    if not isinstance(getattr(self, name), value):
                        return False
                return True
            except Exception:
                return False

        ns['check_annotations'] = check_annotations

        return super().__new__(cls, name, parents, ns)


exec(sys.stdin.read())
