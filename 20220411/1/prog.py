import gettext

translation = gettext.translation("prog", "po", fallback=True)
_, ngettext = translation.gettext, translation.ngettext

def dialog():
    while s := input(_("Input a string: ")):
        n = len(s.split())
        print(ngettext("{} word entered", "{} words entered", n).format(n))

dialog()
print(_("Bye"))
