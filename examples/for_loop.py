from instructions import *

loop_amount = 10
def main():
    hexcode = []
    hexcode.append(stri(False, 0, loop_amount))
    hexcode.append(jmpif(COND_LE, True, 3, 0))
    hexcode.append(subi(0, 0, 1))
    hexcode.append(jumpr(-2))
    hexcode.append(HALT)

    write_to_file(hexcode, 'forloop.bin')

if __name__ == "__main__":
    main()