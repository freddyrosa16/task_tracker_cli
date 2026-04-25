import sys

from add import add


def main():
    file_path = "tasks.json"

    args = sys.argv[1:]
    if len(args) < 2:
        print("Usage: python3 main.py <command> <id> <some description>")

    if args[0] == "add":
        print(add(file_path, args))


if "__main__" == __name__:
    main()
