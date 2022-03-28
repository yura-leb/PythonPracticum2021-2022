"""
Pydocstyle test.

and Docstring in public module.
"""

import sys


class check(type):
    """Class check annotations in type."""

    def __new__(cls, name, parents, ns):
        """Create object."""

        def check_annotations(self):
            """Check annotations."""
            if not hasattr(self, "__annotations__"):
                return True
            try:
                for name, value in self.__annotations__.items():
                    if not isinstance(getattr(self, name), value):
                        return False
                return True
            except Exception:
                return False

        ns["check_annotations"] = check_annotations

        return super().__new__(cls, name, parents, ns)


exec(sys.stdin.read())
