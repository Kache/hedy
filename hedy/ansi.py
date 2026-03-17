from typing import overload

colors = {
    'black': 0,
    'blue': 27,
    'brown': 94,
    'gray': 244,
    'green': 34,
    'orange': 202,
    'pink': 207,
    'purple': 55,
    'red': 1,
    'white': 7,
    'yellow': 3,
}


@overload
def color(code256: int, /) -> str: ...
@overload
def color(r: int, g: int, b: int, /) -> str: ...


def color(*codes: int):
    x_ground = {'fore': 38, 'back': 48}['fore']
    clr_space = {
        1: 5,  # 8-bit
        3: 2,  # 24-bit
    }

    if len(codes) not in clr_space or not all(0 <= c <= 255 for c in codes):
        raise TypeError(f"Invalid args: {codes!r}")

    return sgr(x_ground, clr_space[len(codes)], *codes)


def sgr(*code: int):
    """ANSI Select Graphic Rendition"""
    args = ';'.join(str(int(v)) for v in code)
    return f"\x1b[{args}m"
