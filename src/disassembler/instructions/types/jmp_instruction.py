from ..instruction import Instruction


# Jump instruction, doesn't require any registers.
class JMPInstruction(Instruction):
    def __init__(self, name, destination):
        """
        Inicijalizuje jump instrukciju.

        :param name: Ime instrukcije (npr. "JMP", "JEQ")
        :param destination: Odredište skoka kao broj (labela)
        """
        super().__init__(name)

        self.destination = destination
        self.ordinal_number = None

    def set_ordinal_number(self, ordinal_number):
        """
        Postavlja redni broj koji predstavlja labelu za skok.

        :param ordinal_number: Broj labele (npr. 3 za label3)
        """
        self.ordinal_number = ordinal_number

    def __repr__(self):
        """
        Tekstualna reprezentacija jump instrukcije.

        Prikazuje ime instrukcije i labelu na koju skače.

        :return: String u formatu 'JMP labelX'
        """
        return f"{super().__repr__()} label{self.ordinal_number}\n"
