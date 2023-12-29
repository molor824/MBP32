from instructions import *

"""
str r0, 10
call fib, rjl
halt

fib:
    add rsp, rsp, 16
    ld.u32 rsp[-8], rjl
    ld.u32 rsp[-4], r0
    str r1, 2
    jmp.ge endif, r0, r1

    str.u32 rjl, rsp[-8]
    add rsp, rsp, -16
    ret rjl
endif:
    add r0, r0, -1
    call fib
    ld.u32 RSP[-12], r0
    str.u32 r0, rsp[-4]
    add r0, r0, -2
    call fib
    str.u32 r1, RSP[-12]
    add r0, r0, r1

    str.u32 rjl, rsp[-8]
    add rsp, rsp, -16
    ret rjl
"""

def main():
    hexcode = []
    hexcode.append(stri(False, 0, 10))
    hexcode.append(jalr(imm=2))
    hexcode.append(HALT)
    hexcode.append(addi(RSP, RSP, 16))
    hexcode.append(loadr(U32, RSP, -8, RJL))
    hexcode.append(loadr(U32, RSP, -4, 0))
    hexcode.append(stri(False, 1, 2))
    hexcode.append(jmpif(COND_GE, False, 4, 0, 1))
    hexcode.append(strm(U32, RJL, RSP, -8))
    hexcode.append(addi(RSP, RSP, -16))
    hexcode.append(jumpa(RJL))
    hexcode.append(addi(0, 0, -1))
    hexcode.append(jalr(imm=-9))
    hexcode.append(loadr(U32, RSP, -12, 0))
    hexcode.append(strm(U32, 0, RSP, -4))
    hexcode.append(addi(0, 0, -2))
    hexcode.append(jalr(imm=-13))
    hexcode.append(strm(U32, 1, RSP, -12))
    hexcode.append(add(0, 0, 1))
    hexcode.append(strm(U32, RJL, RSP, -8))
    hexcode.append(addi(RSP, RSP, -16))
    hexcode.append(jumpa(RJL))
    
    write_to_file(hexcode, 'fibonacci_recursive.bin')

if __name__ == "__main__":
    main()