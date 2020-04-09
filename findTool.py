import os
import string
import random


def iterateThroughFolder(pathArg, toFindArg, exclude=(), display=False):
    foundFiles = []
    for pathFile in os.listdir(pathArg):
        if pathFile in exclude:
            continue
        if display:
            print(f"Looking through {pathArg}")
        pathFile = f'{pathArg}{os.sep}{pathFile}'
        if os.path.isfile(pathFile):
            found = findInFile(pathFile, toFindArg)
            if found:
                foundFiles.append((pathFile, found[1]))
        elif os.path.isdir(pathFile):
            foundFiles += iterateThroughFolder(pathFile, toFindArg, display=display)
    return foundFiles


def findInFile(pathFile, toFindArg):
    with open(pathFile, 'r', errors='ignore') as pathOpenFile:
        pathReadFileLines = pathOpenFile.readlines()
        for lineNumber, line in enumerate(pathReadFileLines):
            if toFindArg in line:
                lineInformation = f'Line {lineNumber} at index {line.index(toFindArg)}: {line.strip()}'
                return True, lineInformation


def generateTxt(foundList):
    file = "log.txt"
    if os.path.exists(file):
        os.remove(file)
    with open(file, 'w') as f:
        for item in foundList:
            f.write(f'{item[1]} at {item[0]}')


def hideFile(file, hiddenSteps=50):
    os.chdir("testFolder")
    alphabet = string.ascii_lowercase

    for x in range(hiddenSteps):
        numberOfFolders = random.randint(5, hiddenSteps - x - 5)
        for y in range(numberOfFolders):
            choice = random.choice(alphabet)
            os.mkdir(choice)
            os.chdir(choice)


if __name__ == "__main__":
    filesFound = iterateThroughFolder(os.getcwd(), "mimcha", exclude=('venv', os.path.basename(__file__)), display=False)
    print(filesFound)
    hideFile("lol.txt")