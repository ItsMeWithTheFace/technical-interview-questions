# Given an integer, count the number of 1 bits its binary representation has

def numSetBits(A):
    bits = 0
    while A > 0:
        # when you subtract 1, it finds the first
        # 1 bit from the left and sets it to 0,
        # and everything after it to 1. We & this 
        # result with the original to make all those
        # bits 0 and look for the next 1 to change to 0
        B = A - 1
        A = A & B
        bits += 1
    return bits

print(numSetBits(0))
print(numSetBits(1))
print(numSetBits(15))
print(numSetBits(234234234234))
