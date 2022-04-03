#!/usr/bin/env python3
"""Contains logic for MUD game."""


def completion_list(prefix, source):
    """Create list to complete line."""
    return [s for s in source if s.startswith(prefix)]


class Player:
    """Player which can move."""

    x = 0
    y = 0

    def __init__(self, x=0, y=0):
        """Create player with x, y coordinates."""
        self.x = x
        self.y = y

    def print_player(self):
        """Print players coordinates."""
        print(f'player at {self.x} {self.y}')

    def print_move_error(self):
        """Print move error."""
        print("cannot move")

    def up(self):
        """Move up."""
        if self.y == 0:
            self.print_move_error()
        else:
            self.y -= 1
            self.print_player()

    def down(self):
        """Move down."""
        if self.y == 9:
            self.print_move_error()
        else:
            self.y += 1
            self.print_player()

    def left(self):
        """Move left."""
        if self.x == 0:
            self.print_move_error()
        else:
            self.x -= 1
            self.print_player()

    def right(self):
        """Move right."""
        if self.x == 9:
            self.print_move_error()
        else:
            self.x += 1
            self.print_player()


class Monster:
    """Monster in coordinates x, y named 'name', with hp."""

    name = ''
    hp = 0
    x = 0
    y = 0

    def __init__(self, name, hp, x, y):
        """Create monster with name, hp and coordinates."""
        self.name = name
        self.hp = hp
        self.x = x
        self.y = y

    def decrease_hp(self):
        """Hurt monster."""
        self.hp -= 10
        if self.hp > 0:
            print(f'{self.name} lost 10 hp, now has {self.hp} hp')
        else:
            print(f'{self.name} dies')

    def __str__(self):
        """Get str(monster) with name, coordinates and hp."""
        return f'{self.name} at ({self.x} {self.y}) hp {self.hp}'
