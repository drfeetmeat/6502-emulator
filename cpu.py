class CPU:
    def __init__(self):
        # 64KB of RAM
        self.mem = [0x00 for i in range(2**16)]
        # program counter
        self.pc = 0x0000
        # accumulator
        self.acc = 0x00
        # x and y registers
        self.x = 0x00
        self.y = 0x00
        # Status Registers:
        #   N	Negative
        #   V	Overflow
        #   -	ignored
        #   B	Break
        #   D	Decimal (use BCD for arithmetics)
        #   I	Interrupt (IRQ disable)
        #   Z	Zero
        #   C	Carry
        self.sr = 0b00100000
        # stack pointer
        self.sp = 0x00

    # function to set 1 singular flag
    def set_flag(self, flag, val):
        # sr is 8 bits, to set 1 flag we bit shift 1 to the left by flag (0-7)
        mask = 1 << flag
        # val is the value we want to set the flag to
        if val:
            self.sr |= mask
        else:
            self.sr ^= mask
