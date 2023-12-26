from hex_gen import *
import numpy as np

def main():
    hexcode = np.full(0x100, NOP, dtype=np.uint32)
    hexcode[0] = add(True, False, ZERO, ZERO, 0, 10)
    hexcode[1] = jump_if(COND_LE, True, 0, ZERO, 10)
    hexcode[2] = sub(True, False, 0, ZERO, 0, 1)
    hexcode[3] = jump(False, False, -2)
    hexcode[11] = HALT

    path = 'forloop.bin'
    hexcode.byteswap().tofile(path)

if __name__ == "__main__":
    main()