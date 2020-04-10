import findTool
import os


def test_generateLog() -> None:
    testData = "hmm"
    fileName = "findToolLog.txt"
    findTool.generateLog(testData)
    assert os.path.exists(fileName)
    os.remove(fileName)

    findTool.generateLog(testData, sepFolder=True)
    logPath = os.path.join(os.getcwd(), fileName)
    assert os.path.exists(logPath)
    os.remove(logPath)
    os.chdir("../")
    os.rmdir("Logs")


def test_isHidden() -> None:
    hiddenFileName = ".hidden.txt"
    with open(hiddenFileName, 'w') as f:
        f.write("")
    assert findTool.isHidden(hiddenFileName)
    os.remove(hiddenFileName)

    notHiddenFileName = "notHidden.txt"
    with open(notHiddenFileName, "w") as f:
        f.write("")
    assert not findTool.isHidden(notHiddenFileName)
    os.remove(notHiddenFileName)


def test_findInFile() -> None:
    toFind = "hello"
    fileName = "hello.txt"

    with open(fileName, 'w') as f:
        f.write((toFind + "\n") * 3)
    assert len(findTool.findInFile(fileName, toFind)) == 3

    toFind = "fail"
    assert len(findTool.findInFile(fileName, toFind)) == 0
    os.remove(fileName)


def test_findWithinPath() -> None:
    path = os.getcwd()
    toFind = "hello"
    dummyText = "hello\nhello\nhello\nhello\nhello"
    testFolder = os.path.join(path, "Test Folder")
    testFilename = "test.txt"
    if not os.path.exists(testFolder):
        os.mkdir(testFolder)

    with open(os.path.join(testFolder, testFilename), 'w') as f:
        f.write(dummyText)

    foundList = findTool.findWithinPath(testFolder, toFind)
    foundItem = foundList[0]
    assert foundItem[0] == os.path.join(testFolder, testFilename)
    assert len(foundItem[1]) == 5
    os.chdir(testFolder)
    os.remove(testFilename)
    os.chdir("../")
    os.rmdir(testFolder)
