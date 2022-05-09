import cpu
import opcodes as op

testcpu = cpu.CPU()
rfile = open('prgm.bin','rb')
strlines = [line for line in rfile]
program = [int(strlines[i],2) for i in range(len(strlines))]
print(program)
