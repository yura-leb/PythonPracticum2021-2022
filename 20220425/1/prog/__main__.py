import gettext

translation = gettext.translation("prog", "po", fallback=True)
_ = translation.gettext 


def solve(a,b):
	if a != 0:
		return -b / a
	else:
		return None

if __name__ == "__main__":

    from pyfiglet import figlet_format
    a, b = float(input()), float(input())

    res = solve(a, b)
    if res:
            print(figlet_format(_("Root: {}").format(res), font="graceful"))
    else:
            print_figlet(figlet_format(_("NO ROOTS")))
