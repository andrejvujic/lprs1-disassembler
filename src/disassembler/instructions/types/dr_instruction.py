from ..instruction import Instruction


class DRInstruction(Instruction):
    """
    Predstavlja instrukciju koja koristi dva registra.

    Nasleđuje klasu `Instruction` i dodaje informacije o dva operanda (registra).
    Na primer: `MOV R1, R2` ili `ADD R3, R4`
    """

    def __init__(self, name, first_register, second_register):
        """
        Inicijalizuje instrukciju sa dva registra.

        :param name: Ime instrukcije (npr. "MOV", "ADD")
        :param first_register: Prvi registar (npr. destinacija)
        :param second_register: Drugi registar (npr. izvor)
        """
        super().__init__(name)

        self.first_register = first_register
        self.second_register = second_register

    def __repr__(self):
        """
        Tekstualna reprezentacija instrukcije sa dva registra.

        :return: String u obliku: 'labelX:\nINSTR R1, R2' ili samo 'INSTR R1, R2'
        """
        return f"{super().__repr__()} {self.first_register}, {self.second_register}"
