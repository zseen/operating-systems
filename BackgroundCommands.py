import os
from pathlib import Path


class Commands:
    def __init__(self):
        home = str(Path.home())
        self.currentDirectory = home

    def printCurrentDirectory(self):
        print(self.currentDirectory)

    def createDirectoryPath(self, destination):
        newPath = os.path.join(self.currentDirectory, destination)
        return newPath

    def checkIfFileExists(self, path):
        if os.path.isfile(path) is True:
            return True
        else:
            print("I cannot find " + path)
        return False

    def ls(self, instruction):
        print("")
        print("The content of " + self.currentDirectory + " is: ")

        if len(instruction) == 2 and instruction[1] == "-r":
            for item in reversed(list(os.listdir(self.currentDirectory))):
                print(item)
        else:
            for item in os.listdir(self.currentDirectory):
                print(item)
        print("")

    def cd(self, location):
        newPath = (self.createDirectoryPath((''.join(location))))
        print("")

        if os.path.isdir(newPath):
            self.currentDirectory = newPath
            print("You are in " + self.currentDirectory + " now")
        else:
            print("No such directory to step into, so you are in " + self.currentDirectory)
        print("")