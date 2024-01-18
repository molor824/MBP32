from instructions import *

iter_count = 90

def main():
    hexcode = [
        stri(False, 0, iter_count),
        stri(False, 1, 0),
        stri(False, 3, 1),
        jmpif(COND_LE, True, 9, 0),
        add(5, 1, 3),
        add(6, 2, 4, True),
        mov(1, 3),
        mov(2, 4),
        mov(3, 5),
        mov(4, 6),
        subi(0, 0, imm=1),
        jumpr(-8),
        HALT,
    ]

    write_to_file(hexcode, 'fibonacci.bin')

if __name__ == "__main__":
    main()