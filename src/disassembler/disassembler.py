import os
import re

from .constants import INSTRUCTIONS_LOCATION_INDICATOR
from .instructions.instruction import Instruction
from .instructions.types.jmp_instruction import JMPInstruction


class Disassembler:
    """
    Disassembler za LPRS1 asembler instrukcije.

    Učitava instrukcije iz datoteke instr_rom.vhdl, dekodira ih u
    odgovarajuće objekte instrukcija, dodaje labele za jump instrukcije
    i omogućava eksport u asm format.
    """

    def __init__(self, instruction_rom_file_name: str):
        """
        Inicijalizuje disassembler sa putanjom do instrukcijske ROM datoteke.

        Automatski pokreće proces disasembliranja.

        :param instruction_rom_file_name: Naziv ili putanja ulazne VHDL datoteke
        """
        self.instruction_rom_file_name = instruction_rom_file_name
        self.instruction_rom_file_path = os.path.join(
            os.getcwd(), instruction_rom_file_name
        )

        self.disassemble()

    def disassemble(self):
        """
        Glavni metod koji učitava, dekodira instrukcije i dodaje jump labele.
        """
        self.raw_instructions = self.load_instructions()
        self.instructions = self.decode_instructions()

        self.add_labels_for_jumps()

    def export(self, output_file_name="disassembled.asm"):
        """
        Eksportuje disasemblirane instrukcije u tekstualni ASM fajl.

        Kreira folder "out" u trenutnom direktorijumu ako ne postoji.

        :param output_file_name: Naziv izlazne ASM datoteke (podrazumevano "disassembled.asm")
        """
        output_dir = os.path.join(os.getcwd(), "out")
        os.makedirs(output_dir, exist_ok=True)

        output_file_path = os.path.join(output_dir, output_file_name)

        with open(output_file_path, "w") as f:
            f.write(
                f"// This code is the result of the disassembly of {self.instruction_rom_file_path}\n// LPRS1 disassembler by Andrej Vujić.\n\n\n"
            )
            f.write(".data\n// Data goes here...\n\n")
            f.write(".text\n")

            for instruction in self.instructions:
                f.write(f"{instruction}\n")

    def load_instruction_rom_content(self):
        with open(self.instruction_rom_file_path, "r") as f:
            raw_content = f.readlines()
        return raw_content

    def load_instructions(self):
        """
        Učitava asemblirane instrukcije iz instrukcijskog ROMa.

        Traži liniju sa indikatorom lokacije instrukcija i zatim
        izdvaja stringove unutar navodnika, koji predstavljaju
        instrukcije koje je LPRS1 assembler generisao.

        :return: Lista binarnih stringova koji predstavljaju instrukcije
        :raises Exception: Ako ne može pronaći instrukcije ili nisu validne
        """
        raw_content = self.load_instruction_rom_content()

        start_index = raw_content.index(INSTRUCTIONS_LOCATION_INDICATOR)

        instructions = []

        for index in range(start_index + 1, len(raw_content)):
            if raw_content[index] == INSTRUCTIONS_LOCATION_INDICATOR:
                break

            matches = re.findall(r'"(.*?)"', raw_content[index])
            if not matches:
                raise Exception("Error while parsing instruction rom!")

            instructions.append(matches[0])

        return instructions

    def decode_instructions(self):
        """
        Pretvara sirove binarne stringove instrukcija u objekte tipa Instruction.

        :return: Lista objekata instrukcija
        """
        instructions = []

        for raw_instruction in self.raw_instructions:
            instructions.append(
                Instruction.from_raw_instruction(raw_instruction)
            )

        return instructions

    def add_labels_for_jumps(self):
        """
        Dodaje labele na instrukcije koje su odredište jump instrukcija.

        Svakoj jump instrukciji dodeljuje jedinstven redni broj
        koji se koristi u nazivu labele.
        """
        jump_number = 0
        for instruction in self.instructions:
            if isinstance(instruction, JMPInstruction):
                instruction.set_ordinal_number(jump_number)
                self.instructions[instruction.destination].set_label_number(
                    jump_number)
                jump_number += 1
