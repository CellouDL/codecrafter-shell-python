import sys
import os

def echo(args):
    print(" ".join(args))

def exit0():
    quit()

def main():

    commands = ["echo", "exit", "type"]
    paths = os.environ.get("PATH").split(":")
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input()
        cmd, *args = command.split(" ")
        if command=="exit 0":
            exit0()
        elif cmd=="echo":
            echo(args)
        elif cmd=="type":
            cmd = args[0]
            path = None
            for i in paths:
                if os.path.isfile(f"{i}/{cmd}"):
                    path = f"{i}/{cmd}"
            if args[0] in commands:
                sys.stdout.write(f"{cmd} is a shell builtin\n")
            elif path:
                sys.stdout.write(f"{cmd} is {path}\n")
            else:
                sys.stdout.write(f"{cmd} not found\n")

        else:
            sys.stdout.write(f"{cmd}: command not found\n")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
