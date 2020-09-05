from sys import stdout


def clear():
    # might need module 'reprint'..
    stdout.write("\x1b[2J\x1b[H")


def go_back(line: int):
    stdout.write(f"\x1b[{line}F")
