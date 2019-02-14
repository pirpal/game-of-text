#!usr/bin/python3
# coding: utf-8

from lib.character import Character

class Number(Character):
    """
    0 1 2 3 4 5 6 7 8 9
    """
    def __init__(self, code, x, y):
        super(code, x, y)
        self.has_operator = False
