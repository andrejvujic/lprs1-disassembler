from ..instruction import Instruction


class SRInstruction(Instruction):
    """
    Predstavlja instrukciju koja koristi jedan registar.

    Nasleđuje klasu `Instruction` i dodaje informaciju o jednom registru.
    Na primer: `INC R1` ili `NOT R2`
    """

    def __init__(self, name, register):
        """
        Inicijalizuje instrukciju sa jednim registrom.

        :param name: Ime instrukcije (npr. "INC", "NOT")
        :param register: Registar na kome se operacija izvodi
        """
        super().__init__(name)
        self.register = register

    def __repr__(self):
        """
        Tekstualna reprezentacija instrukcije sa jednim registrom.

        :return: String u obliku: 'labelX:\nINSTR R1' ili samo 'INSTR R1'
        """
        return f"{super().__repr__()} {self.register}"
