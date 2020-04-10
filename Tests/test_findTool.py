import findTool
import os


def test_generateLog():
    testData = "hmm"
    fileName = "findToolLog.txt"
    findTool.generateLog(testData)
    assert os.path.exists(fileName)

    os.remove(fileName)
    findTool.generateLog(testData, sepFolder=True)
    logPath = os.path.join(os.getcwd(), fileName)
    assert os.path.exists(logPath)


def test_findInFile():
    pass
