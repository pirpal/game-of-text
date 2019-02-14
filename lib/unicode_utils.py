#!usr/bin/python3
# coding: utf-8

from lib.constants import *
from lib.console_ui import *

"""
A collection of functions to play with unicode
"""


def getUnicodes(chr_type: str):
    """
    print system available unicodes
    for a given character type
    """
    print(f"\n{chr_type.capitalize()} unicodes:")
    for i in UNICODES[chr_type]:
        offset = "  " if i < 100 else " "
        print(f"{offset}{i}: {chr(i)}")

def printCharset():
    """
    Used to build charset table, see ./charset.org
    """
    print("Game of text charset")
    for n in CHARACTERS.items():
        print(f"{n[0]} :")
        if n[0] == "numbers":
            for c in n[1]:
                print(f"{c}: {ord(str(c))}")
        else:
            for c in n[1]:
                print(f"{c}: {ord(c)}")

def initGrid(size, data):
    """
    initGrid(int, dict) => [[int]]
    
    The world is modelized as a 2d list of int
    representing chars unicodes
    An empty cell is 0

    data is a dictionnary with format:
    {
        chr: [(x1, y1), (x2, y2), (x3, y3), etc.]
    }

    where (x1, y1) gives the position of a chr in the grid

    Example grid filled with some "a" and "z":
    g = initGrid(
        10, # size
        {
        
        }
    )
    """
    grid = [[0 for i in range(size)] for i in range(size)]
    for k in data.items():
        pass
    # TODO

    return grid
    
