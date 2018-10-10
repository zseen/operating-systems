import os

class CommandPrompt:
    def __init__(self):
        self.currentDirectory = "C:\\Users"

    def runCommand(self):
        while True:
            command = input("What should I do? Type 'ls' to see my content or 'exit' to...exit!: ")

            if command == "ls":
                print(os.listdir("C:\\Users"))

            if command == "exit":
                break




def main():
    command = CommandPrompt()
    command.runCommand()

if __name__ == "__main__":
    main()