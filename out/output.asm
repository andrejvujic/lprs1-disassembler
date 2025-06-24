// This code is the result of the disassembly of /Users/andrej/Documents/Python/LPRS1 Disassembler/in/instruction_rom.vhdl
// LPRS1 disassembler by Andrej Vujić.


.data
// Data goes here...

.text
inc R0, R0
inc R0, R0
ld R0, R0
inc R1, R1

label1:
sub R7, R0, R2
jmpz label0

shl R1, R1
inc R2, R2
jmp label1


label0:
sub R2, R2, R2
inc R5, R5
inc R5, R5
inc R5, R5
inc R5, R5

label3:
sub R7, R0, R2
jmpz label2

add R3, R5, R2
ld R3, R3
add R4, R4, R3
inc R2, R2
jmp label3


label2:
add R4, R4, R1
shr R4, R4
shr R4, R4
sub R0, R0, R0
ld R0, R0
st R4, R0
sub R1, R1, R1
inc R1, R1
sub R0, R0, R0
inc R0, R0
ld R0, R0
st R1, R0

label4:
jmp label4

