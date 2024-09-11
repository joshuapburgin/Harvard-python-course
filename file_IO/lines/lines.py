import sys
import os

def main():
    print(sys.argv[1][-3:])

    if len(sys.argv)<2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1][-3:]!=".py":
        sys.exit("Not a Python file")
    elif not os.path.exists(sys.argv[1]):
        sys.exit("File does not exist")
    else:
        print(count_lines(sys.argv[1]))



def count_lines(code_file):
    with open(code_file) as file:
        code= file.readlines()

    line_count=0
    for line in code:
        stripped_line = line.strip()

        # Check if the line is not empty and does not start with a hashtag
        if stripped_line and not stripped_line.startswith("#"):
            line_count += 1
    return line_count

if __name__ == "__main__":
    main()



