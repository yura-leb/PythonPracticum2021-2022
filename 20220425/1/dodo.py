DOIT_CONFIG = {'default_tasks': ['babel', 'test', 'wheel', 'sdist', 'cleanup']}

def task_babel():
    """Make translation po file."""
    return {
            "actions": [
                "pybabel extract -o po/prog.pot prog.py",
                "pybabel update -D prog -i po/prog.pot -d po -l ru",
                "pybabel compile -D prog -d po -l ru"
            ],
            "file_dep": ["prog.py"],
            "targets": ["po/prog.pot", "po/ru/LC_MESSAGES/prog.mo"]
           }

def task_wheel():
    """Create wheel."""
    return {
            "actions": ['python -m build -w'],
            "file_dep": ["prog.py", "po/ru/LC_MESSAGES/prog.mo"],
    }

def task_sdist():
    """Create tar."""
    return {
            "actions": ['python -m build -s'],
            "file_dep": ["prog.py", "po/ru/LC_MESSAGES/prog.mo"],
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
            "actions": ["rm -f po/prog.pot", "rm -f po/ru/LC_MESSAGES/prog.mo"],
   }

