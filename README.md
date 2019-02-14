Game of Text
------------

**Game of Text** is an exotic and experimental variant of game of
life.

# World

The world of **Game of Text** is a two-dimensional array of dimensions
80x80.

The world is created by parsing any code source file.
Space and tabulations are empty cells on which characters can move.


## Characters

The world is filled with characters are grouped in families defining
behavior :

| Family           | Characters                      |
|------------------|---------------------------------|
| Upcase letters   | `A`-`Z`                         |
| Downcase letters | `a` - `z`                       |
| Numbers          | `0` - `9`                       |
| Operators        | `+` `-` `/` `*` `%` `=` `<` `>` |
| Brackets         | `(` `)` `{` `}` `[` `]`         |
| Punctuations     | `!` `,` `.` `:` `;` `?`         |
| Hyphens          | `-` `_`                         |
| Specials         | `#` `$` `&` `@` `&#x7c;` `~`    |


