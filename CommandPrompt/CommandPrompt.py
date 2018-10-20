import CommandExecutor as CLE

INITIAL_HELP = ("Options:" '\n'
                "'ls' to see my content, " '\n'
                "'ls -r' to see my content reversed, "  '\n'
                "'cat <file>' to see the content of a text file, " '\n'
                "'printTogether <file1> <file2>' to print two text files together," '\n'
                "'joinTogether <file1> <file2> <file3>' merge file1 and file2 into file3," '\n'
                "'mkdir <name>' to create a folder, " '\n'
                "'rm <name>' to delete a file, " '\n'
                "'head <file> <x>' to see the first x lines of a file, " '\n'
                "'cd <somewhere>' to go somewhere, " '\n'
                "'cd ..' to go back to the previous level directory, or " '\n'
                "'exit' to...exit! " '\n')


class CommandPrompt:
    def __init__(self):
        self.commandExecutor = CLE.CommandExecutor()

    def run(self):
        print(INITIAL_HELP)

        while True:
            print(self.commandExecutor.getCurrentDirectory())
            command = input("What should I do?: ")
            request = command.split()

            if request[0] == "ls":
                self.ls(request)

            if request[0] == "cd":
                if request[1] == "..":
                    self.getParentDirectory()
                else:
                    self.cd(request[1:])

            if request[0] == "joinTogether" and len(request) == 4:
                self.joinTogether(request[1], request[2], request[3])

            if request[0] == "printTogether" and len(request) == 3:
                self.printTogether(request[1], request[2])

            if request[0] == "cat" and len(request) == 2:
                self.cat(request[1])

            if request[0] == "mkdir" and len(request) == 2:
                self.mkdir(request[1])

            if request[0] == "rm" and len(request) == 2:
                self.rm(request[1])

            if request[0] == "head" and len(request) == 3:
                self.head(request[1], request[2])

            if command == "exit":
                exit(0)

    def ls(self, request):
        print("")
        print("The content of " + self.commandExecutor.getCurrentDirectory() + " is:")
        content = self.commandExecutor.listDirectoryContent(request)
        for folder in content:
            print(folder)
        print("")

    def cd(self, location):
        newPath = self.commandExecutor.changeDirectory(location)
        if newPath is False:
            print("Directory does not exist.")
        else:
            print("You are in " + self.commandExecutor.getCurrentDirectory() + " now.")

    def getParentDirectory(self):
        if self.commandExecutor.goBackOneLevel():
            print("You are in " + self.commandExecutor.getCurrentDirectory() + " now.")
        else:
            print("Root level reached")

    def cat(self, file):
        lines = self.commandExecutor.getFileContent(file)
        if lines:
            for line in lines:
                print(line)
        else:
            print("I cannot find this file.")

    def printTogether(self, file1, file2):
        lines = self.commandExecutor.printTwoFilesTogether(file1, file2)
        if lines:
            for line in lines:
                print(line, end="")
            print("")
        else:
            print("Please double-check your files.")

    def joinTogether(self, file1, file2, file3):
        lines = self.commandExecutor.joinTwoFilesTogetherInThird(file1, file2, file3)
        if lines:
            for line in lines:
                print(line, end="")
            print("")
        else:
            print("Please double-check your files.")

    def mkdir(self, name):
        isCreated = self.commandExecutor.makeDirectory(name)
        path = CLE.FH.createDirectoryPath(self.commandExecutor.getCurrentDirectory(), name)
        if isCreated:
            print("Your new folder is ready! It is called " + name + " and is here: " + path)
        else:
            print("Folder already exists")

    def rm(self, file):
        if self.commandExecutor.removeFile(file):
            print(file + " removed.")
        else:
            print("I cannot find this file.")

    def head(self, file, linesNum):
        lines = self.commandExecutor.getTextLinesFromBeginning(file, linesNum)
        if lines:
            for line in lines:
                print(line)
            print("")
        else:
            print("I cannot find this file.")


def main():
    cp = CommandPrompt()
    cp.run()


if __name__ == "__main__":
    main()
