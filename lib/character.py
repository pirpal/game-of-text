#!usr/bin/python3
# coding: utf-8


class Character:
    """
    Parent class for all characters used in the game
    """
    def __init__(self, code: int, x: int, y: int):
        """
        code: int -> character unicode
        x:    int -> x pos in world
        y:    int -> y pos in world
        """
        self.code = code
        self.x = x
        self.y = y
        self.color = self.setColor()

    def setColor(self):
        """ setColor() -> string """
        if self.code in UNICODES["upletters"]:
            return "blue"
        elif self.code in UNICODES["downletters"]:
            return "grey"
        elif self.code in UNICODES["numbers"]:
            return "white"
        elif self.code in UNICODES["brackets"]:
            return "yellow"
        elif self.code in UNICODES["operators"]:
            return "green"
        elif self.code in UNICODES["puncts"]:
            return "red"
        elif self.code in UNICODES["quotes"]:
            return "cyan"
        elif self.code in UNICODES["hyphen"]:
            return "magenta"
        elif self.code in UNICODES["specials"]:
            return "red"

    def isUpLetter(self):
        """ isUpLetter() -> bool """
        return self.code in UNICODES["upletters"]

    def isDownLetter(self):
        """ isDownLetter() -> bool """
        return self.code in UNICODES["downletters"]

    def isNumber(self):
        """ isNumber() -> bool """
        return self.code in UNICODES["numbers"]

    def isBracket(self):
        """ isBracket() -> bool """
        return self.code in UNICODES["brackets"]

    def isOperator(self):
        """ isOperator() -> bool """
        return self.code in UNICODES["operators"]

    def isPunctuation(self):
        """ isPunctuation() -> bool """
        return self.code in UNICODES["puncts"]

    def isQuote(self):
        """ isQuote() -> bool """
        return self.code in UNICODES["quotes"]

    def isHyphen(self):
        """ isHyphen() -> bool """
        return self.code in UNICODES["hyphens"]

    def isSpecial(self):
        """ isSpecial() -> bool """
        return self.code in UNICODES["specials"]
