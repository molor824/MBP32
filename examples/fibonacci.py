from hex_gen import *
import numpy as np

iter_count = 90

hexcode = np.full(0x100, NOP, dtype=np.uint32)
hexcode[0] = add(True, False, 0, immediate=iter_count)
hexcode[1] = add(True, False, 1, immediate=0)
hexcode[2] = add(True, False, 2, immediate=0)
hexcode[3] = add(True, False, 3, immediate=1)
hexcode[4] = add(True, False, 4, immediate=0)
hexcode[5] = jump_if(COND_LE, True, 9, 0)
hexcode[6] = add(False, False, 5, 1, 3)
hexcode[7] = add(False, True, 6, 2, 4)
hexcode[8] = add(True, False, 1, 3)
hexcode[9] = add(True, False, 2, 4)
hexcode[10] = add(True, False, 3, 5)
hexcode[11] = add(True, False, 4, 6)
hexcode[12] = sub(True, False, 0, 0, immediate=1)
hexcode[13] = jump(False, -8)
hexcode[14] = HALT

hexcode.byteswap().tofile("fibonacci.bin")