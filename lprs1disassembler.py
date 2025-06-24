#!/usr/bin/env python3

"""
    LPRS1 Disassembler
    Disasembler za asembler korišten na predmetu Logičko projektovanje računarskih sistema 1.
    
    Autor: Andrej Vujić
    24. jun 2025.
"""

import sys

from src.disassembler.disassembler import Disassembler


def disassemble(instruction_rom_file_name, output_file_name="disassembled.asm"):
    disassembler = Disassembler(
        instruction_rom_file_name=instruction_rom_file_name
    )
    disassembler.export(output_file_name=output_file_name)


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) < 1 or len(args) > 2:
        print("Error! Incorrect usage of disassembler.\nExample of correct usage:\nlprs1disassembler instruction_rom.vhdl")
        exit()

    if len(args) > 1:
        disassemble(args[0], args[1])
    else:
        disassemble(args[0])
