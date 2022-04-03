"""Module to run MUD cmd."""

import shlex
import cmd
from MUD.logic import Player, Monster, completion_list


class repl(cmd.Cmd):
    """Class to run cmd."""

    prompt = "> "

    def __init__(self):
        """Init cmd, dungeon and player."""
        cmd.Cmd.__init__(self)
        self.width = 10
        self.height = 10
        self.dungeon = [[[] for _ in range(self.height)]
                        for i in range(self.width)]
        self.player = Player()

    def print_monsters(self, x, y):
        """Print all monsters in cell."""
        for monster in self.dungeon[x][y]:
            print(monster)

    def do_add(self, arg):
        """Add monster with name and hp in coordinates."""
        args = shlex.split(arg, comments=True)
        if len(args) == 8:
            name = args[2]
            hp, x, y = map(int, (args[4], args[-2], args[-1]))
            self.dungeon[x][y].append(Monster(name, hp, x, y))

    def do_show(self, arg):
        """Show all monsters in dungeon."""
        args = shlex.split(arg, comments=True)
        if len(args) == 1:
            for x in range(len(self.dungeon)):
                for y in range(len(self.dungeon[x])):
                    self.print_monsters(x, y)

    def do_move(self, arg):
        """Move up, down, left or right."""
        args = shlex.split(arg, comments=True)
        if len(args) == 1 and args[0] in ('up', 'down', 'left', 'right'):
            eval(f'self.player.{args[0]}()')
            monsters = self.dungeon[self.player.x][self.player.y]
            if monsters:
                output = 'encountered: '
                for monster in monsters:
                    output += f'{monster.name} {monster.hp} hp, '
                print(output[:-2])

    def do_attack(self, arg):
        """Attack monster with 'name'."""
        args = shlex.split(arg, comments=True)
        if len(args) == 1:
            name = args[0]
            monster_to_attack = None
            for monster in self.dungeon[self.player.x][self.player.y]:
                if monster.name == name:
                    monster_to_attack = monster
            if monster_to_attack:
                monster_to_attack.decrease_hp()
                if monster_to_attack.hp <= 0:
                    self.dungeon[self.player.x][self.player.y].remove(
                        monster_to_attack)
            else:
                print(f'no {name} here')

    def complete_add(self, prefix, allcommand, beg, end):
        """Compete cmd add."""
        if allcommand.count(' ') == 1:
            return completion_list(prefix, ['monster'])
        elif allcommand.count(' ') == 2:
            return completion_list(prefix, ['name'])
        elif allcommand.count(' ') == 4:
            return completion_list(prefix, ['hp'])
        elif allcommand.count(' ') == 6:
            return completion_list(prefix, ['coords'])

    def complete_attack(self, prefix, allcommand, beg, end):
        """Complete cmd attack."""
        if allcommand.count(' ') == 1:
            monster_names = [
                monster.name
                for monster in self.dungeon[self.player.x][self.player.y]
            ]
            for i in range(len(monster_names)):
                if monster_names[i].count(' '):
                    monster_names[i] = f'"{monster_names[i]}"'
            return completion_list(prefix, monster_names)

    def complete_show(self, prefix, allcommand, beg, end):
        """Complete cmd show."""
        if allcommand.count(' ') == 1:
            return completion_list(prefix, ['monsters'])

    def complete_move(self, prefix, allcommand, beg, end):
        """Complete cmd move."""
        if allcommand.count(' ') == 1:
            return completion_list(prefix, ['up', 'down', 'left', 'right'])

    def do_exit(self, arg):
        """Exit command line."""
        return True
