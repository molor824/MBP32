from instructions import *

iter_count = 90

def main():
    hexcode = []
    hexcode.append(stri(False, 0, iter_count))
    hexcode.append(stri(False, 1, 0))
    hexcode.append(stri(False, 3, 1))
    hexcode.append(jmpif(COND_LE, True, 9, 0))
    hexcode.append(add(5, 1, 3))
    hexcode.append(add(6, 2, 4, True))
    hexcode.append(mov(1, 3))
    hexcode.append(mov(2, 4))
    hexcode.append(mov(3, 5))
    hexcode.append(mov(4, 6))
    hexcode.append(subi(0, 0, imm=1))
    hexcode.append(jumpr(-8))
    hexcode.append(HALT)

    write_to_file(hexcode, 'fibonacci.bin')

if __name__ == "__main__":
    main()