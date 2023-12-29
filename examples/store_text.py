from instructions import *

text = "Hello World!"
def main():
    print('\n'.join(map(hex, text.encode())))

    hexcode = []
    for b in text.encode():
        hexcode.append(loadi(imm1=b))
        hexcode.append(addi(RSP, RSP, 1))
    hexcode.append(HALT)
    write_to_file(hexcode, 'storetext.bin')

if __name__ == "__main__":
    main()