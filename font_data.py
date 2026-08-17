# This Python file uses the following encoding: utf-8
from dataclasses import dataclass

@dataclass
class Glyph:
    left: int = 0
    glyph_width: int = 0
    char_width: int = 0

font_data = {
    "a": Glyph(2, 19, 23),
    "B": Glyph(2, 22, 26),
    "o": Glyph(2, 20, 24),
    "r": Glyph(2, 14, 18),
    "d": Glyph(2, 19, 23),
    "G": Glyph(2, 25, 29),
    "m": Glyph(1, 27, 30),
    " ": Glyph(15, 0, 15),
    "l": Glyph(2, 5, 9),
    "i": Glyph(2, 5, 9),
    "I": Glyph(2, 5, 9),
    "n": Glyph(2, 18, 22),
    "y": Glyph(2, 20, 24),
    "u": Glyph(2, 18, 22),
    "t": Glyph(2, 14, 18),
    "W": Glyph(-1, 32, 30),
    "T": Glyph(2, 24, 28),
    "s": Glyph(2, 19, 23),
    "c": Glyph(2, 20, 24),
    "f": Glyph(2, 14, 18),
    "'": Glyph(2, 5, 9),
    "e": Glyph(2, 20, 24),
    ",": Glyph(4, 6, 14),
    "h": Glyph(2, 18, 22),
    "!": Glyph(6, 6, 18)
}

if __name__ == "__main__":
    pass
