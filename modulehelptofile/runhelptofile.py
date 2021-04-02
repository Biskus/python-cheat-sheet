import sys
import os 

def gethelp(topic):
    fname = f'_help_{topic}'
    os.system(f'python helptofile.py {topic} > {fname}')
    return open(fname).read()


def main():
    print(gethelp(sys.argv[1]))


if __name__ == '__main__':
    main()