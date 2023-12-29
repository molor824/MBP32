from instructions import *

# Increments register by 1 and then repeats
# This results in an infinite loop of incrementing a register
# Used for testing performance by running the simulation for t amount of time
# Instruction speed would be: r0 * 2 / t
# Last test: 210 instructions/sec

hexcode = []
hexcode.append(addi(0, 0, 1))
hexcode.append(jumpr(-1))  

write_to_file(hexcode, 'test.bin')