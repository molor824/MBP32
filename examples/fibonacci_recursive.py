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
    hexcode = [
        stri(False, 0, 8),
        jalr(imm=2),
        HALT,
        addi(RSP, RSP, 16),
        load(U32, RSP, -8, RJL),
        load(U32, RSP, -4, 0),
        stri(False, 1, 2),
        jmpif(COND_GE, False, 4, 0, 1),
        strm(U32, RJL, RSP, -8),
        addi(RSP, RSP, -16),
        jumpa(RJL),
        addi(0, 0, -1),
        jalr(imm=-9),
        load(U32, RSP, -12, 0),
        strm(U32, 0, RSP, -4),
        addi(0, 0, -2),
        jalr(imm=-13),
        strm(U32, 1, RSP, -12),
        add(0, 0, 1),
        strm(U32, RJL, RSP, -8),
        addi(RSP, RSP, -16),
        jumpa(RJL),
    ]
    
    write_to_file(hexcode, 'fibonacci_recursive.bin')

if __name__ == "__main__":
    main()