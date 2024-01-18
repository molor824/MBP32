from instructions import *

loop_amount = 1_000_000
def main():
    hexcode = [
        stri(False, 0, loop_amount),
        jmpif(COND_LE, True, 3, 0),
        subi(0, 0, 1),
        jumpr(-2),
        HALT,
    ]

    write_to_file(hexcode, 'forloop.bin')

if __name__ == "__main__":
    main()