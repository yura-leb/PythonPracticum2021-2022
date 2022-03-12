import readline
import shlex
import cmd

dungeon = [[[] for _ in range(10)] for i in range(10)]

def completion_list(prefix, source):
    return [s for s in source if s.startswith(prefix)]

class Player:
    x = 0
    y = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def print_player(self):
        print(f'player at {self.x} {self.y}')

    def print_move_error(self):
        print("cannot move")
        
    def up(self):
        if self.y == 0:
            self.print_move_error()
        else:
            self.y -= 1
            self.print_player()

    def down(self):
        if self.y == 9:
            self.print_move_error()
        else:
            self.y += 1
            self.print_player()

    def left(self):
        if self.x == 0:
            self.print_move_error()
        else:
            self.x -= 1
            self.print_player()

    def right(self):
        if self.x == 9:
            self.print_move_error()
        else:
            self.x += 1
            self.print_player()


class Monster:
    name = ''
    hp = 0
    x = 0
    y = 0

    def __init__(self, name, hp, x, y):
        self.name = name
        self.hp = hp
        self.x = x
        self.y = y

    def decrease_hp(self):
        self.hp -= 10
        if self.hp > 0:
            print(f'{self.name} lost 10 hp, now has {self.hp} hp')
        else:
            print(f'{self.name} dies')

    def __str__(self):
        return f'{self.name} at ({self.x} {self.y}) hp {self.hp}'



def print_monsters(x, y):
    for monster in dungeon[x][y]:
        print(monster)


player = Player()

class repl(cmd.Cmd):
    prompt = "> "

    def do_add(self, arg):
        """
        Adds monster with name and hp in coordinates
        """
        args = shlex.split(arg, comments=True)
        if len(args) != 8: 
            return
        name = args[2]
        hp, x, y = map(int, (args[4], args[-2], args[-1]))
        dungeon[x][y].append(Monster(name, hp, x, y))
    
    def do_show(self, arg):
        """
        Shows all monsters in dungeon
        """
        args = shlex.split(arg, comments=True)
        if len(args) == 1:
            for x in range(len(dungeon)):
                for y in range(len(dungeon[x])):
                    print_monsters(x, y)

    def do_move(self, arg):
        """
        Move up, down, left or right
        """
        args = shlex.split(arg, comments=True)
        if len(args) == 1 and args[0] in ('up', 'down', 'left', 'right'):
            eval(f'player.{args[0]}()')
            monsters = dungeon[player.x][player.y]
            if monsters:
                output = 'encountered: '
                for monster in monsters:
                    output += f'{monster.name} {monster.hp} hp, '
                print(output[:-2])


    def do_attack(self, arg):
        """
        Attacks monster with <name>
        """
        args = shlex.split(arg, comments=True)
        if len(args) == 1:
            name = args[0]
            monster_to_attack = None
            for monster in dungeon[player.x][player.y]:
                if monster.name == name:
                    monster_to_attack = monster
            if monster_to_attack:
                monster_to_attack.decrease_hp()
                if monster_to_attack.hp <= 0:
                    dungeon[player.x][player.y].remove(monster_to_attack)
            else:
                print(f'no {name} here')


    def complete_add(self, prefix, allcommand, beg, end):
        if allcommand.count(' ') == 1:
            return completion_list(prefix, ['monster'])
        elif allcommand.count(' ') == 2:
            return completion_list(prefix, ['name'])
        elif allcommand.count(' ') == 4:
            return completion_list(prefix, ['hp'])

        elif allcommand.count(' ') == 6:
            return completion_list(prefix, ['coords'])

    def complete_attack(self, prefix, allcommand, beg, end):
        if allcommand.count(' ') == 1:
            monster_names = [monster.name for monster in dungeon[player.x][player.y]]
            for i in range(len(monster_names)):
                if monster_names[i].count(' '):
                    monster_names[i] = f'"{monster_names[i]}"'
            return completion_list(prefix, monster_names)
    
    def complete_show(self, prefix, allcommand, beg, end):
        if allcommand.count(' ') == 1:
            return completion_list(prefix, ['monsters'])

    def complete_move(self, prefix, allcommand, beg, end):
        if allcommand.count(' ') == 1:
            return completion_list(prefix, ['up', 'down', 'left', 'right'])

    def do_exit(self, arg):
        """Exit command line"""
        return True

repl().cmdloop()
