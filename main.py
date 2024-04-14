from SPI import build
import os
import logging

#logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def main():

    path = "program.txt"
    if os.path.isfile(path):
        with open(path) as f:
            program = f.read()
            build(program)


if __name__ == '__main__':
    main()

