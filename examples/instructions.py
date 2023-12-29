ARITHMETICS = 0b00
MEMORY = 0b01
CONDITIONAL = 0b10

COND_EQ = 0b010
COND_NE = 0b101
COND_LT = 0b100
COND_GT = 0b001
COND_LE = 0b110
COND_GE = 0b011

RZ = 0xf
RSP = 0xe
RJL = 0xd

NOP = 0b11
HALT = 0b11 | (1 << 31)

S32 = 0b100
S16 = 0b101
S8 = 0b110
U32 = 0b000
U16 = 0b001
U8 = 0b010

def get_imm(imm: int):
    return (int(imm) & 0xffff) << 8
def get_rs1(rs1: int):
    return (int(rs1) & 0xf) << 24
def get_rs2(rs2: int):
    return (int(rs2) & 0xf) << 20
def get_rd(rd: int):
    return (int(rd) & 0xf) << 28

def add(rd = RZ, rs1 = RZ, rs2 = RZ, carry = False):
    return ARITHMETICS | get_rd(rd) | get_rs1(rs1) | get_rs2(rs2) | bool(carry) << 6
def sub(rd = RZ, rs1 = RZ, rs2 = RZ, carry = False):
    return add(rd, rs1, rs2, carry) | 1 << 5
def shl(rd = RZ, rs1 = RZ, rs2 = RZ, carry = False):
    return add(rd, rs1, rs2, carry) | 1 << 4
def shr(rd = RZ, rs1 = RZ, rs2 = RZ, carry = False):
    return shl(rd, rs1, rs2, carry) | 1 << 5
def sha(rd = RZ, rs1 = RZ, rs2 = RZ, carry = False):
    return shl(rd, rs1, rs2, carry) | 1 << 7
def _and(rd = RZ, rs1 = RZ, rs2 = RZ):
    return ARITHMETICS | 1 << 3 | get_rd(rd) | get_rs1(rs1) | get_rs2(rs2)
def _or(rd = RZ, rs1 = RZ, rs2 = RZ):
    return _and(rd, rs1, rs2) | 0b01 << 4
def _xor(rd = RZ, rs1 = RZ, rs2 = RZ):
    return _and(rd, rs1, rs2) | 0b10 << 4
def _not(rd = RZ, rs1 = RZ):
    return _and(rd, rs1) | 0b11 << 4
def addi(rd = RZ, rs1 = RZ, imm = 0, carry = False):
    return ARITHMETICS | get_rd(rd) | get_rs1(rs1) | get_imm(imm) | 1 << 2 | bool(carry) << 6
def subi(rd = RZ, rs1 = RZ, imm = 0, carry = False):
    return addi(rd, rs1, imm, carry) | 1 << 5
def shli(rd = RZ, rs1 = RZ, imm = 0, carry = False):
    return addi(rd, rs1, imm, carry) | 1 << 4
def shri(rd = RZ, rs1 = RZ, imm = 0, carry = False):
    return shli(rd, rs1, imm, carry) | 1 << 5
def shai(rd = RZ, rs1 = RZ, imm = 0, carry = False):
    return shli(rd, rs1, imm, carry) | 1 << 7
def _andi(rd = RZ, rs1 = RZ, imm = 0):
    return ARITHMETICS | 1 << 3 | get_rd(rd) | get_rs1(rs1) | get_imm(imm)
def _ori(rd = RZ, rs1 = RZ, imm = 0):
    return _andi(rd, rs1, imm) | 0b01 << 4
def _xori(rd = RZ, rs1 = RZ, imm = 0):
    return _andi(rd, rs1, imm) | 0b10 << 4
def stri(upper = False, rd = RZ, imm = 0):
    return MEMORY | get_rd(rd) | get_imm(imm) | bool(upper) << 5
def strm(size = U32, rd = RZ, rs1 = RSP, imm = 0):
    return MEMORY | 1 << 4 | get_rd(rd) | get_rs1(rs1) | get_imm(imm) | (int(size) & 0b111) << 4
def mov(rd = RZ, rs1 = RZ):
    return MEMORY | 1 << 3 | get_rd(rd) | get_rs1(rs1)
def loadi(rs1 = RSP, imm = 0, imm1 = 0):
    return MEMORY | 1 << 2 | get_rs1(rs1) | get_imm(imm) | (int(imm1) & 0xf) << 4 | (int(imm1) & 0xf0) << 20
def loadr(size = U32, rs1 = RSP, imm = 0, rd = RZ):
    return MEMORY | 1 << 2 | 1 << 3 | get_rd(rd) | get_imm(imm) | get_rs1(rs1) | (int(size) & 0b111) << 4
def jumpr(imm = 0):
    return CONDITIONAL | 0b111 << 2 | get_imm(imm)
def jumpa(rs1 = RSP, imm = 0):
    return jumpr(imm) | get_rs1(rs1) | 1 << 6
def jalr(rd = RJL, imm = 0):
    return CONDITIONAL | get_imm(imm) | get_rd(rd)
def jala(rd = RJL, rs1 = RSP, imm = 0):
    return jalr(rd, imm) | get_rs1(rs1) | 1 << 6
def jmpif(condition = COND_EQ, signed = False, imm = 0, rs1 = RZ, rd = RZ):
    return CONDITIONAL | (int(condition) & 0b111) << 2 | bool(signed) << 7 | get_rs1(rs1) | get_rd(rd) | get_imm(imm)
def setif(condition = COND_EQ, signed = False, rd = RZ, rs1 = RZ, rs2 = RZ):
    return CONDITIONAL | (int(condition) & 0b111) << 2 | bool(signed) << 7 | 1 << 5 | get_rd(rd) | get_rs1(rs1) | get_rs2(rs2)
def setifi(condition = COND_EQ, signed = False, rd = RZ, rs1 = RZ, imm = 0):
    return setif(condition, signed, rd, rs1, 0) | get_imm(imm) | 1 << 6

import struct

def write_to_file(instructions: list[int], filepath: str):
    file = open(filepath, 'wb')
    file.write(struct.pack(">{}I".format(len(instructions)), *instructions))

    file.close()