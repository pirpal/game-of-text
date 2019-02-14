#!usr/bin/python3
# coding: utf-8

# Constants ---------------------------------------------------------
ALPHABET     = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

CHARACTERS_FAMILIES = [
    "upletters", "downletters", "numbers", "brackets",
    "operators", "puncts", "hyphens", "specials"
]

CHARACTERS = {
    "upletters":   list(ALPHABET),
    "downletters": list(ALPHABET.lower()),
    "numbers":     list(range(10)),
    "brackets":    list("()[]{}"),
    "operators":   list("+-*/%<>="),
    "puncts":      list(",?;.:!"),
    "quotes":      list("\"'"),
    "hyphens":     list("-_"),
    "specials":    list("$@#"),
}

UNICODES = { # see ./charset.org
    "upletters":   list(range(65, 91)),
    "downletters": list(range(97, 123)),
    "numbers":     list(range(48, 58)),
    "brackets":    [40, 41, 91, 93, 123, 125],
    "operators":   [37, 42, 43, 45, 47, 60, 61, 62],
    "puncts":      [33, 44, 46, 58, 59, 63],
    "quotes":      [34, 39],
    "hyphens":     [45, 95],
    "specials":    [35, 36, 38, 64, 124, 126],
}

