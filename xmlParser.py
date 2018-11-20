import sys

def parse(content):
    print(content)

def main():
    file = open(sys.argv[1],"r")
    contents = file.read()
    contents = contents.split("<ad>")
    file.close()
    for content in contents:
        parse(content)

if __name__ == "__main__":
    main()
