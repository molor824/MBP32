from hex_gen import *
import numpy as np

"""
add r0, ZERO, iter_count
add r1, ZERO, 0
add r2, ZERO, 1
while r0 > 0:
    add r3, r1, r2
    add r1, r2, 0
    add r2, r3, 0
    sub r0, r0, 1
add r0, r1, 0
"""

iter_count = 40

hexcode = np.full(0x100, NOP, dtype=np.uint32)
hexcode[0] = add(True, False, 0, immediate=iter_count)
hexcode[1] = add(True, False, 1, immediate=0)
hexcode[2] = add(True, False, 2, immediate=1)
hexcode[3] = jump_if(COND_LE, True, 6, 0)
hexcode[4] = add(False, False, 3, 1, 2)
hexcode[5] = add(True, False, 1, 2, immediate=0)
hexcode[6] = add(True, False, 2, 3, immediate=0)
hexcode[7] = sub(True, False, 0, 0, immediate=1)
hexcode[8] = jump(False, -5)
hexcode[9] = add(True, False, 0, 1, immediate=0)
hexcode[10] = HALT

hexcode.byteswap().tofile("fibonacci.bin")