import os


def hideFile(file):
    if os.name == "posix":
        os.rename(file, f".{file}")


def revealFile(file):
    if os.name == "posix":
        if not str(file).startswith("."):
            return
        os.rename(file, file[1:])
