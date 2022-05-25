DOIT_CONFIG = {'default_tasks': ['babel', 'test', 'wheel', 'sdist', 'cleanup']}

po = "po"
def task_babel():
    """Make translation po file."""
    return {
            "actions": [
                f"pybabel extract -o {po}/prog.pot prog/__main__.py",
                f"pybabel update -D prog -i {po}/prog.pot -d {po} -l ru",
                f"pybabel compile -D prog -d {po} -l ru"
            ],
            "file_dep": ["prog/__main__.py"],
            "targets": [f"{po}/prog.pot", f"{po}/ru/LC_MESSAGES/prog.mo"]
           }

def task_wheel():
    """Create wheel."""
    return {
            "actions": ['python3 -m build -w'],
            "file_dep": ["prog/__main__.py", f"{po}/ru/LC_MESSAGES/prog.mo"],
    }

def task_sdist():
    """Create tar."""
    return {
            "actions": ['python3 -m build -s'],
            "file_dep": ["prog/__main__.py", f"{po}/ru/LC_MESSAGES/prog.mo"],
    }


def task_test():
    """Test prog.py."""
    return {
        "actions": ["python3 -m unittest -v"],
        #"file_dep": ["test_prog.py"]
    }


def task_cleanup():
    """Remove all."""
    return {
            "actions": [f"rm -f {po}/prog.pot", f"rm -f {po}/ru/LC_MESSAGES/prog.mo"],
   }

