import os


def hideFile(file, hiddenSteps=50):
    if not os.path.exists(os.getcwd() + os.sep + "testFolder"):
        os.mkdir("testFolder")
    os.chdir("testFolder")
    alphabet = string.ascii_lowercase

    for x in range(hiddenSteps):
        numberOfFolders = random.randint(3, 5)
        for y in range(numberOfFolders):
            choice = random.choice(alphabet)
            os.mkdir(choice)
            os.chdir(choice)