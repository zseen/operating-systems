import os
from pathlib import Path


def getHomeDirectory():
    home = str(Path.home())
    return home

def createDirectoryPath(currentDirectory, destination):
    newPath = os.path.join(currentDirectory, destination)
    return newPath

def checkIfFileExists(path):
    return os.path.isfile(path)

def checkIfDirectoryExists(path):
    return os.path.isdir(path)

def isRootLevel(path):
    return path == str(Path.home())

def getParentDirectory(path):
    return Path(path).parent




