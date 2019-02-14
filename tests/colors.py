#!usr/bin/python3

from termcolor import colored

def testConsoleColors():
    """
    not really a test, just to show and configure term colors
    """
    for c in "red blue cyan green grey yellow magenta white".split(" "):
        text = colored("Hello world!", c)
        print(text)

testConsoleColors()
