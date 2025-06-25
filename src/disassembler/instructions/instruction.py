from ..constants import *
from ..operations.operation import Operation
from ..registers.register import Register


class Instruction:
    """
    Predstavlja apstraktnu instrukciju u LPRS1 disassembler-u.
    Na osnovu sirove binarne instrukcije, bira odgovarajući tip instrukcije
    (bez registra, sa jednim, dva ili tri registra) i instancira odgovarajuću klasu.
    """

    def __init__(self, name: str):
        """
        Inicijalizuje osnovnu instrukciju sa imenom.

        :param name: Ime instrukcije (npr. "ADD", "JMP", "MOV" itd.)
        """
        self.name = name
        self.label_number = None

    def set_label_number(self, label_number: int):
        """
        Dodjeljuje broj labeli koji će biti prikazan ispred instrukcije (npr. label3:).

        :param label_number: Broj koji predstavlja labelu
        """
        self.label_number = label_number

    @staticmethod
    def from_raw_instruction(raw_instruction: str) -> 'Instruction':
        """
        Kreira instancu instrukcije na osnovu sirove binarne string reprezentacije.

        :param raw_instruction: Binarni string dužine `EXPECTED_INSTRUCTION_LEN`
        :return: Instanca jedne od podklasa Instruction-a (JMPInstruction, SRInstruction, DRInstruction, TRInstruction)
        :raises Exception: Ako je dužina instrukcije pogrešna ili tip ne postoji
        """
        if len(raw_instruction) != EXPECTED_INSTRUCTION_LEN:
            raise Exception(
                "Error while parsing instructions! Incorrect instruction length."
            )

        instruction_code, raw_rz, raw_rx, raw_ry, jmp_destination = Instruction.split_raw_instruction(
            raw_instruction
        )

        operation = Operation.from_instrution_code(instruction_code)

        if not operation.number_of_registers:
            from .types.jmp_instruction import JMPInstruction
            return JMPInstruction(
                name=operation.name,
                destination=jmp_destination
            )

        registers = {
            "RZ": Register(raw_rz),
            "RX": Register(raw_rx),
            "RY": Register(raw_ry),
        }

        if operation.is_single_register():
            from .types.sr_instruction import SRInstruction
            return SRInstruction(
                name=operation.name,
                register=registers[operation.registers[0]]
            )

        if operation.is_double_register():
            from .types.dr_instruction import DRInstruction
            return DRInstruction(
                name=operation.name,
                first_register=registers[operation.registers[0]],
                second_register=registers[operation.registers[1]]
            )

        if operation.is_triple_register():
            from .types.tr_instruction import TRInstruction
            return TRInstruction(
                name=operation.name,
                first_register=registers[operation.registers[0]],
                second_register=registers[operation.registers[1]],
                third_register=registers[operation.registers[2]]
            )

        raise Exception(
            "Error! There are no instructions with more than 3 registers!"
        )

    @staticmethod
    def split_raw_instruction(raw_instruction: str) -> tuple[str, str, str, str, int]:
        """
        Parsira sirovu binarnu instrukciju i odvaja je na dijelove: šifra instrukcije, registri i destinacija za skok.

        :param raw_instruction: Binarni string instrukcije
        :return: Tuple: (šifra instrukcije, RZ, RX, RY, destinacija skoka)
        """
        instruction_code = raw_instruction[INSTRUCTION_CODE_START_IDX: INSTRUCTION_CODE_END_IDX + 1]
        rz = raw_instruction[RZ_START_IDX: RZ_END_IDX + 1]
        rx = raw_instruction[RX_START_IDX: RX_END_IDX + 1]
        ry = raw_instruction[RY_START_IDX: RY_END_IDX + 1]

        raw_jmp_destination = raw_instruction[JMP_DESTINATION_START_IDX: JMP_DESTINATION_END_IDX + 1]
        jmp_destination = Instruction.parse_jmp_destination(
            raw_jmp_destination)

        return instruction_code, rz, rx, ry, jmp_destination

    @staticmethod
    def parse_jmp_destination(raw_jmp_destination: str) -> int:
        """
        Pretvara binarnu string reprezentaciju destinacije za skok u cjelobrojnu vrednost.

        :param raw_jmp_destination: Binarni string (npr. "0000010010")
        :return: Decimalna vrednost destinacije
        """
        length = len(raw_jmp_destination) - 1
        index = length
        jmp_destination = 0

        while index >= 0:
            bit = int(raw_jmp_destination[index])
            jmp_destination += pow(2, length - index) * bit
            index -= 1

        return jmp_destination

    def __repr__(self) -> str:
        """
        Tekstualna reprezentacija instrukcije. Ako je labela dodeljena, biće prikazana ispred.

        :return: Formatiran string instrukcije
        """
        if self.label_number is not None:
            return f"\nlabel{self.label_number}:\n{self.name}"
        return self.name
