# Addressing modes:

# ACC       Accumulator
# ABS	    absolute
# ABS_X	    absolute, X-indexed
# ABS_Y	    absolute, Y-indexed
# IMM       immediate
# IMPL	    implied
# IND	    indirect
# X_IND	    X-indexed, indirect
# IND_Y	    indirect, Y-indexed
# REL	    relative
# ZPG	    zeropage
# ZPG_X	    zeropage, X-indexed
# ZPG_Y	    zeropage, Y-indexed


#immediate

# 0x09 boolean or accumulator with the data in the next memory address and store it in the accumulator
def ORA_IMM(CPU):
    CPU.pc += 1
    CPU.acc |= CPU.mem[CPU.pc]
    if CPU.acc < 0:
        CPU.set_flag(7,1)
    if CPU.acc.did_overflow:
        CPU.set_flag(6,1)
    if CPU.acc == 0:
        CPU.set_flag(1,1)

# 0x29 boolean and accumulator with the data in the next memory address and store it in the accumulator
def AND_IMM(CPU):
    CPU.pc += 1
    CPU.acc &= CPU.mem[CPU.pc]

# 0x49 boolean exclusive or accumulator with data in the next memory address and store it in the accumulator
def EOR_IMM(CPU):
    CPU.pc += 1
    CPU.acc ^= CPU.mem[CPU.pc]

# 0x69 add accummulator with the data in the next memory address with the carry in and store it in the accumulator
def ADC_IMM(CPU):
    CPU.pc += 1
    #CPU.acc =

# 0xA9 - load accumulator with the data in the next memory address
def LDA_IMM(CPU):
    CPU.pc += 1
    CPU.acc = CPU.mem[CPU.pc]

# 0xA2 - load x with with the data in the next memory address
def LDX_IMM(CPU):
    CPU.pc += 1
    CPU.x = CPU.mem[CPU.pc]

# 0xA0 - load y with with the data in the next memory address
def LDY_IMM(CPU):
    CPU.pc += 1
    CPU.y = CPU.mem[CPU.pc]

opcodes = {
    0x09 : ORA_IMM,
    0xA0 : LDY_IMM,
    0xA2 : LDX_IMM,
    0xA9 : LDA_IMM,
}
