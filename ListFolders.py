import os


class Actions:
    def __init__(self):
        self.currentDirectory = "C:\\Users"
        print(self.currentDirectory)

    def ls(self):
        print("")
        print("The content of " + self.currentDirectory + " is: ")
        for item in os.listdir(self.currentDirectory):
            print(item)
        print("")

    def cd(self, instruction):
        directoryBeforeChange = self.currentDirectory
        self.currentDirectory += "\\"
        self.currentDirectory += ' '.join(instruction[1:])
        path = self.currentDirectory
        if os.path.isdir(path):
            print("You are in " + self.currentDirectory + " now")
        else:
            self.currentDirectory = directoryBeforeChange
            print("No such directory, I will return to " + self.currentDirectory )
            






class CommandPrompt(Actions):

    def runCommand(self):
        while True:
            command = input("What should I do? Type 'ls' to see my content, 'cd <somewhere>' to go somewhere  or 'exit' to...exit!: ")



            if command == "ls":
                self.ls()

            goToLocation = command.split()
            if goToLocation[0] == "cd":
                self.cd(goToLocation)




            if command == "exit":
                break




def main():
    command = CommandPrompt()
    command.runCommand()

if __name__ == "__main__":
    main()