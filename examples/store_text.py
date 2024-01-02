from instructions import *

text = "Hello World!"
def main():
    encoded = text.encode()

    print('\n'.join(map(hex, encoded)))

    hexcode = [stri(rd=0), stri(rd=1)]

    for b in encoded:
        hexcode.append(stri(rd=0, imm=b))
        hexcode.append(load(U8, RSP, 0, 0))
        hexcode.append(addi(RSP, RSP, 1))

    hexcode.append(HALT)

    write_to_file(hexcode, 'storetext.bin')

if __name__ == "__main__":
    main()