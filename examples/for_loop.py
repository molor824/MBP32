from hex_gen import *
import numpy as np

hexcode = np.full(0x100, NOP, dtype=np.uint32)
hexcode[0] = add(True, False, 0, immediate=10)
hexcode[1] = jump_if(COND_LE, True, 10, 0)
hexcode[2] = sub(True, False, 0, 0, immediate=1)
hexcode[3] = jump(False, -2)
hexcode[11] = HALT

hexcode.byteswap().tofile("forloop.bin")