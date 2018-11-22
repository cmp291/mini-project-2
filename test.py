import sys

def main():
    file = open(sys.argv[1],"r")
    contents = file.read()
    file.close()
    file = open(sys.argv[2],"r")
    contents2 = file.read()
    file.close()

if __name__ == "__main__":
        main()
