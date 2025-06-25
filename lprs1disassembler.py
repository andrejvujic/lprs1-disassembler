#!/usr/bin/env python3

"""
    LPRS1 Disassembler
    Disasembler za asembler korišten na predmetu Logičko projektovanje računarskih sistema 1.
    
    Autor: Andrej Vujić
    24. jun 2025.
"""

import argparse
import sys

from src.disassembler.disassembler import Disassembler


def disassemble(instruction_rom_file_name, data_ram_file_name=None, output_file_name=None):
    disassembler = Disassembler(
        instruction_rom_file_name=instruction_rom_file_name,
        data_ram_file_name=data_ram_file_name,
    )
    disassembler.export(output_file_name=output_file_name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("irf")
    parser.add_argument("-drf", "--data-ram-file")
    parser.add_argument("-o", "--output-file")

    args = parser.parse_args()

    disassemble(
        args.irf,
        data_ram_file_name=args.data_ram_file,
        output_file_name=args.output_file
    )
