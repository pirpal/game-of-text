#!usr/bin/python3
# coding: utf-8

from lib.constants import UNICODES

"""
Console output functions
"""

def showGrid(g):
    """
    showGrid([[int]]) => None
    """
    for row in g:
        print("\t", end="")
        for elt in row:
            if elt == 0:
                print(".", end="  ")

def tab():
    print("\t", end="")
        
def header(title):
    print("\n")
    tab()
    print("-" * 70)
    print(f"\t\tGame of Text - {title}")
    tab()
    print("-" * 70)
    print("\n")
