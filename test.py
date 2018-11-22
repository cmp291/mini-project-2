import sys

def main():
    file = open(sys.argv[1],"r")
    contents = file.read()
    file.close()
    contents = contents.split("\n")
    file = open(sys.argv[2],"r")
    contents2 = file.read()
    file.close()
    contents2 = contents2.split("\n")
    if contents == contents2:
        print("True")
    else:
        print("False")

if __name__ == "__main__":
        main()
