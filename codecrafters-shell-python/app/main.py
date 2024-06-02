import sys


def main():

    commands = ["echo", "exit", "type"]
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input()
        if command=="exit 0":
            break
        elif command.startswith("echo "):
            print(command[5:])
        elif command.startswith("type "):
            if command[5:] in commands:
                sys.stdout.write(f"{command[5:]} is a shell builtin\n")
            else:
                sys.stdout.write(f"{command[5:]} not found\n")

        else:
            sys.stdout.write(f"{command}: command not found\n")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
