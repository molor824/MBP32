import numpy as np

CATEGORIES = {
    'arithmetic' : 0b00,
    'memory' : 0b01,
    'condition' : 0b10,
    'other' : 0b11,
}

RJL = 0xd
RSP = 0xe
ZERO = 0xf

NOP = 0b11
HALT = 0b11 | (1 << 31)

def jump(link: bool, absolute: bool, immediate: int, rs1: int = ZERO, rd: int = ZERO):
    instruction = CATEGORIES['condition']
    instruction |= (0b000 if link else 0b111) << 2
    instruction |= bool(absolute) << 6
    instruction |= (int(immediate) & 0xffff) << 8
    instruction |= (int(rd) & 0xf) << 28
    instruction |= (int(rs1) & 0xf) << 24
    return instruction

"""
rs1 - left hand operand
rd - right hand operand
"""
def jump_if(condition: int, signed: bool, rs1: int, rd: int, immediate: int = 0):
    instruction = CATEGORIES['condition']
    instruction |= (int(condition) & 0b111) << 2
    instruction |= (int(signed) & 0b1) << 7
    instruction |= (int(rd) & 0b1111) << 28
    instruction |= (int(rs1) & 0b1111) << 24
    instruction |= (int(immediate) & 0xffff) << 8
    return instruction

def set_if(condition: int, signed: bool, isimmediate: bool, rs1: int, rs2: int, immediate: int = 0, rd: int = RJL):
    instruction = CATEGORIES['condition']
    instruction |= (int(condition) & 0b111) << 2
    instruction |= 1 << 5
    instruction |= bool(isimmediate) << 6
    instruction |= bool(signed) << 7
    instruction |= (int(rd) & 0xf) << 28
    instruction |= (int(rs1) & 0xf) << 24
    instruction |= (int(rs2) & 0xf) << 20
    instruction |= (int(immediate) & 0xffff) << 8
    return instruction

def main():
    hexcode = [NOP] * 2
    hexcode.append(jump(True, False, 8, ZERO, RJL))
    hexcode.append(NOP)
    hexcode.append(jump(False, True, 0, ZERO))

    for _ in range(8):
        hexcode.append(NOP)
    hexcode.append(jump(False, True, 0, RJL))

    print('\n'.join(hex(h) for h in hexcode))

    path = 'hexcode.bin'
    np.array(hexcode, dtype=np.uint32).byteswap().tofile(path)

if __name__ == "__main__":
    main()