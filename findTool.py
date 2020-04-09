import os
import sys
import copy


def findWithinPath(pathArg, toFindArg, exclude=(), display=True):
    pathArg = os.path.abspath(pathArg)
    foundFiles = []
    for file in os.listdir(pathArg):
        if file in exclude:
            continue
        pathFile = os.path.join(pathArg, file)
        if os.path.isfile(pathFile):
            if display:
                print(f"Looking in {pathFile}")
            found = findInFile(pathFile, toFindArg)
            if len(found) != 0:
                foundFiles.append((pathFile, found))
        elif os.path.isdir(pathFile):
            if display:
                print(f"Looking through {pathFile}")
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


def generateLog(info, file="findToolLog.txt", path=os.getcwd(), sepFolder=False):
    path = os.path.abspath(path)
    os.chdir(path)
    if sepFolder:
        folderName = "Logs"
        path = os.path.join(path, folderName)
        if not os.path.exists(path):
            os.mkdir(folderName)
        os.chdir(path)
    with open(file, 'w') as f:
        f.write(info)
    print(f"{file} generated at {path}.")


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
    logFileName = "findToolLog.txt"
    baseFile = os.path.basename(__file__)
    excludePaths = ("venv", baseFile, "findToolLog.txt", logFileName)
    display = True
    moreInfo = True
    sysArgs = sys.argv

    if len(sysArgs) == 1:
        path = os.getcwd()
        find = "mimcha"
    else:
        find = sysArgs[1]
        sysArgs = sysArgs[2:]
        copySysArgs = copy.copy(sysArgs)
        for arg in sysArgs:
            flag = True
            if arg == "-more":
                moreInfo = True
            elif arg == "-nomore":
                moreInfo = False
            elif arg == "-display":
                display = True
            elif arg == "-nodisplay":
                display = False
            else:
                flag = False

            if flag:
                copySysArgs.remove(arg)

        if len(copySysArgs) == 0:
            path = os.getcwd()
        else:
            if len(copySysArgs) == 1:
                path = copySysArgs[0]
                if not os.path.exists(path):
                    print(f"The path '{path}' does not exist.")
                    return
            else:
                print("Incorrect arguments given. Syntax: python findtool.py [find] [path] "
                      "(Path can be left empty to refer to current path)")
                return

    filesFound = findWithinPath(path, find, exclude=excludePaths, display=display)
    toLog = generatePrettyText(filesFound, find, moreInfo=moreInfo)
    generateLog(toLog, path=path, sepFolder=True)


if __name__ == "__main__":
    main()
