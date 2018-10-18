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
                "'cd..' to go back to the previous level directory, or " '\n'
                "'exit' to...exit! " '\n')

class CommandPrompt(object):
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
                self.cd(request[1:])
            #
            # if request[0] == "joinTogether" and len(request) == 4:
            #     self.joinTogether(request[1], request[2], request[3])
            #
            # if request[0] == "printTogether" and len(request) == 3:
            #     self.printTogether(request[1], request[2])
            #
            if request[0] == "cat" and len(request) == 2:
                self.cat(request[1])
            #
            # if request[0] == "mkdir" and len(request) == 2:
            #     self.mkdir(request[1])
            #
            # if request[0] == "rm" and len(request) == 2:
            #     self.rm(request[1])
            #
            # if request[0] == "head" and len(request) == 3:
            #     self.head(request[1], request[2])

            if command == "exit":
                exit(0)

    def ls(self, request):
        print("")
        print("The content of " + self.commandExecutor.getCurrentDirectory() + " is:")
        content = self.commandExecutor.ls(request)
        for folder in content:
            print(folder)
        print("")

    def cd(self, location):
        currentPath = self.commandExecutor.getCurrentDirectory()
        newPath = self.commandExecutor.cd(location)

        if newPath is False:
            print("Directory does not exist.")
        elif currentPath == newPath:
            print("You cannot go up, as you have reached root level.")
        else:
            print("You are in " + newPath + " now.")

    def cat(self, file):







def main():
    cp = CommandPrompt()
    cp.run()


if __name__ == "__main__":
    main()