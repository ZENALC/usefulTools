import os
import sys


def findWithinPath(pathArg, toFindArg, exclude=(), display=False):
    foundFiles = []
    for file in os.listdir(pathArg):
        if file in exclude:
            continue
        if display:
            print(f"Looking through {pathArg}")
        pathFile = f'{pathArg}{os.sep}{file}'
        if os.path.isfile(pathFile):
            found = findInFile(pathFile, toFindArg)
            if len(found) != 0:
                foundFiles.append((pathFile, found))
        elif os.path.isdir(pathFile):
            foundFiles += findWithinPath(pathFile, toFindArg, display=display, exclude=exclude)
    return foundFiles


def findInFile(pathFile, toFindArg):
    foundInfo = []
    with open(pathFile, 'r', errors='ignore') as pathOpenFile:
        pathReadFileLines = pathOpenFile.readlines()
        for lineNumber, line in enumerate(pathReadFileLines):
            if toFindArg in line:
                lineInformation = f'Line {lineNumber} at index {line.index(toFindArg)}: {line.strip()}'
                foundInfo.append(lineInformation)
    return foundInfo


def generateLog(info, file="log.txt", path=os.getcwd()):
    os.chdir(path)
    with open(file, 'w') as f:
        f.write(info)
    print(f"{file} generated.")


def generatePrettyText(foundList, toFindArg, moreInfo=True):
    if moreInfo:
        totalString = f"Detailed information of files found with keyword '{toFindArg}':\n\n"
    else:
        totalString = f"Files found with keyword '{toFindArg}':\n\n"

    first = True
    for fileInfo in foundList:
        if first:
            totalString += f"{fileInfo[0]}\n"
            first = False
        else:
            if moreInfo:
                totalString += f"\n{fileInfo[0]}\n"
            else:
                totalString += f"{fileInfo[0]}\n"
        if moreInfo:
            for foundInfo in fileInfo[1]:
                totalString += f"{foundInfo}\n"
    return totalString


def main():
    logFileName = "log.txt"
    base = os.path.basename(__file__)
    excludePaths = ("venv", base, "log.txt", logFileName)

    if len(sys.argv) == 3:
        find = sys.argv[1]
        path = sys.argv[2]
    elif len(sys.argv) == 2:
        path = os.getcwd()
        find = sys.argv[1]
    elif len(sys.argv) == 1:
        path = os.getcwd()
        find = "mimcha"
    else:
        print("Incorrect number of arguments given. Syntax: python findtool.py [find] [path] "
              "(Path can be left empty to refer to current path)")
        return

    filesFound = findWithinPath(path, find, exclude=excludePaths, display=True)
    toLog = generatePrettyText(filesFound, find, moreInfo=True)
    generateLog(toLog, path=path)


if __name__ == "__main__":
    main()
