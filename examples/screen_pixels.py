from instructions import *

pixel = [
    0b1000000000000000,
    0b0100000000000000,
    0b0010000000000000,
    0b0001000000000000,
    0b0000100000000000,
    0b0000010000000000,
    0b0000001000000000,
    0b0000000100000000,
    0b0000000010000000,
    0b0000000001000000,
    0b0000000000100000,
    0b0000000000010000,
    0b0000000000001000,
    0b0000000000000100,
    0b0000000000000010,
    0b0000000000000001,
]
def main():
    hexcode = []

    for i, p in enumerate(pixel):
        hexcode.append(stri(False, 0, p))
        hexcode.append(shli(0, 0, 16))
        hexcode.append(bitori(0, 0, 1 << i))
        hexcode.append(gpout(0))
    
    hexcode.append(jumpa(RZ, 0))

    write_to_file(hexcode, 'screen_pixels.bin')

if __name__ == "__main__":
    main()