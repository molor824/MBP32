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
S24 = 0b101
S16 = 0b110
S8 = 0b111
U32 = 0b000
U24 = 0b001
U16 = 0b010
U8 = 0b011

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
def bitand(rd = RZ, rs1 = RZ, rs2 = RZ):
    return ARITHMETICS | 1 << 3 | get_rd(rd) | get_rs1(rs1) | get_rs2(rs2)
def bitor(rd = RZ, rs1 = RZ, rs2 = RZ):
    return bitand(rd, rs1, rs2) | 0b01 << 4
def bitxor(rd = RZ, rs1 = RZ, rs2 = RZ):
    return bitand(rd, rs1, rs2) | 0b10 << 4
def bitnot(rd = RZ, rs1 = RZ):
    return bitand(rd, rs1) | 0b11 << 4
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
def bitandi(rd = RZ, rs1 = RZ, imm = 0):
    return ARITHMETICS | 1 << 3 | get_rd(rd) | get_rs1(rs1) | get_imm(imm)
def bitori(rd = RZ, rs1 = RZ, imm = 0):
    return bitandi(rd, rs1, imm) | 0b01 << 4
def bitxori(rd = RZ, rs1 = RZ, imm = 0):
    return bitandi(rd, rs1, imm) | 0b10 << 4
def stri(signed = False, rd = RZ, imm = 0):
    return MEMORY | get_rd(rd) | get_imm(imm) | bool(signed) << 6
def strm(size = U32, rd = RZ, rs1 = RSP, imm = 0):
    return MEMORY | 1 << 3 | get_rd(rd) | get_rs1(rs1) | get_imm(imm) | (int(size) & 0b111) << 4
def mov(rd = RZ, rs1 = RZ):
    return add(rd, rs1)
def load(size = U32, rs1 = RSP, imm = 0, rd = RZ):
    return MEMORY | 1 << 2 | get_rd(rd) | get_imm(imm) | get_rs1(rs1) | (int(size) & 0b111) << 4
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

    print("hex code:")
    
    for i in instructions:
        print(f"{hex(i & 0xffffffff)[2:]:0>8}")
        packed = struct.pack(">I", i)
        file.write(packed)

    file.close()