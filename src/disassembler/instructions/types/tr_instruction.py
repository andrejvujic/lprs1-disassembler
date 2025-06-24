from ..instruction import Instruction


class TRInstruction(Instruction):
    """
    Predstavlja instrukciju koja koristi tri registra.

    Nasleđuje klasu `Instruction` i dodaje informacije o tri operanda (registra).
    Npr. `ADD R1, R2, R3` ili `SUB R4, R5, R6`
    """

    def __init__(self, name, first_register, second_register, third_register):
        """
        Inicijalizuje instrukciju sa tri registra.

        :param name: Ime instrukcije (npr. "ADD", "SUB")
        :param first_register: Prvi registar (npr. rezultat ili destinacija)
        :param second_register: Drugi registar (npr. operand A)
        :param third_register: Treći registar (npr. operand B)
        """
        super().__init__(name)

        self.first_register = first_register
        self.second_register = second_register
        self.third_register = third_register

    def __repr__(self):
        """
        Tekstualna reprezentacija instrukcije sa tri registra.

        :return: String u obliku: 'labelX:\nINSTR R1, R2, R3' ili samo 'INSTR R1, R2, R3'
        """
        return f"{super().__repr__()} {self.first_register}, {self.second_register}, {self.third_register}"
