ARITHMETICS = 0b00
CONDITIONAL = 0b10

COND_EQ = 0b010
COND_NE = 0b101
COND_LT = 0b100
COND_GT = 0b001
COND_LE = 0b110
COND_GE = 0b011

ZERO = 0xf
RSP = 0xe
RJL = 0xd

NOP = 0b11
HALT = 0b11 | (1 << 31)

def get_imm(imm: int):
    return (int(imm) & 0xffff) << 8
def get_rs1(rs1: int):
    return (int(rs1) & 0xf) << 24
def get_rs2(rs2: int):
    return (int(rs2) & 0xf) << 20
def get_rd(rd: int):
    return (int(rd) & 0xf) << 28

def jump(absolute: bool, immediate: int, rs1: int = ZERO):
    instruction = CONDITIONAL
    instruction |= 0b111 << 2
    instruction |= bool(absolute) << 6
    instruction |= get_imm(immediate) | get_rs1(rs1)
    return instruction
def jump_link(absolute: bool, immediate: int, rs1: int = ZERO, rd: int = RJL):
    instruction = CONDITIONAL
    instruction |= bool(absolute) << 6
    instruction |= get_imm(immediate) | get_rs1(rs1) | get_rd(rd)
    return instruction
def jump_if(condition: int, signed: bool, immediate: int, rs1: int = ZERO, rd: int = ZERO):
    instruction = CONDITIONAL
    instruction |= (int(condition) & 0b111) << 2
    instruction |= (int(signed) & 0b1) << 7
    instruction |= get_rs1(rs1) | get_rd(rd) | get_imm(immediate)
    return instruction

def set_if(condition: int, signed: bool, isimmediate: bool, rd: int, rs1: int, rs2: int = ZERO, immediate: int = 0):
    instruction = CONDITIONAL
    instruction |= (int(condition) & 0b111) << 2
    instruction |= 1 << 5
    instruction |= bool(isimmediate) << 6
    instruction |= bool(signed) << 7
    instruction |= get_rd(rd) | get_rs1(rs1)
    instruction |= get_imm(immediate) if isimmediate else get_rs2(rs2)
    return instruction

def add(isimmediate: bool, carry: bool, rd: int, rs1: int = ZERO, rs2: int = ZERO, immediate: int = 0):
    instruction = ARITHMETICS
    instruction |= bool(isimmediate) << 2
    instruction |= bool(carry) << 6
    instruction |= get_rs1(rs1) | get_rd(rd)
    instruction |= get_imm(immediate) if isimmediate else get_rs2(rs2)
    return instruction
def sub(isimmediate: bool, carry: bool, rd: int, rs1: int = ZERO, rs2: int = ZERO, immediate: int = 0):
    instruction = add(isimmediate, carry, rd, rs1, rs2, immediate)
    instruction |= 1 << 5
    return instruction
def shl(isimmediate: bool, rd: int, rs1: int = ZERO, rs2: int = ZERO, immediate: int = 0):
    instruction = add(isimmediate, False, rd, rs1, rs2, immediate)
    instruction |= 1 << 4
    return instruction
def shr(isimmediate: bool, rd: int, rs1: int = ZERO, rs2: int = ZERO, immediate: int = 0):
    instruction = sub(isimmediate, False, rd, rs1, rs2, immediate)
    instruction |= 1 << 4
    return instruction
def sha(isimmediate: bool, rd: int, rs1: int = ZERO, rs2: int = ZERO, immediate: int = 0):
    instruction = sub(isimmediate, False, rd, rs1, rs2, immediate)
    instruction |= 1 << 4
    instruction |= 1 << 7
    return instruction
def bit_and(isimmediate: bool, rd: int, rs1: int = ZERO, rs2: int = ZERO, immediate: int = 0):
    instruction = ARITHMETICS
    instruction |= bool(isimmediate) << 2
    instruction |= 1 << 3
    instruction |= get_rs1(rs1) | get_rd(rd)
    instruction |= get_imm(immediate) if isimmediate else get_rs2(rs2)
    return instruction
def bit_or(isimmediate: bool, rd: int, rs1: int = ZERO, rs2: int = ZERO, immediate: int = 0):
    instruction = bit_and(isimmediate, rd, rs1, rs2, immediate)
    instruction |= 1 << 4
    return instruction
def bit_xor(isimmediate: bool, rd: int, rs1: int = ZERO, rs2: int = ZERO, immediate: int = 0):
    instruction = bit_and(isimmediate, rd, rs1, rs2, immediate)
    instruction |= 2 << 4
    return instruction
def bit_not(isimmediate: bool, rd: int, rs1: int = ZERO, immediate: int = 0):
    instruction = bit_and(isimmediate, rd, rs1, ZERO, immediate)
    instruction |= 3 << 4
    return instruction
