from table import table
import sys

def main(args):
    print(table[int(args)])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: asciicode <code>")
    else:
        main(sys.argv[1])