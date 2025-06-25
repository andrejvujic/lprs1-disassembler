class Operation:
    """
    Predstavlja operaciju (instrukciju) procesora.

    Svaka instanca sadrži:
    - ime instrukcije (npr. "add", "jmp")
    - listu registara koje instrukcija koristi (npr. ["RZ", "RX"])
    - broj registara (izvedeno iz dužine liste registara)
    - tip instrukcije (npr. "00", "01")
    - šifru operacije (npr. "0001")
    """

    def __init__(self, name, registers, type, operation_code):
        """
        Inicijalizuje operaciju sa zadatim parametrima.

        :param name: Ime instrukcije
        :param registers: Lista imena registara koje instrukcija koristi
        :param type: Tip instrukcije kao string
        :param operation_code: Šifra operacije kao string
        """
        self.name = name
        self.registers = registers
        self.number_of_registers = len(registers)
        self.type = type
        self.operation_code = operation_code

    @staticmethod
    def from_instrution_code(instruction_code):
        """
        Vrati instancu Operation za dati kod instrukcije.

        :param instruction_code: Šifra instrukcije kao string (npr. "000001")
        :return: Instanca klase Operation koja odgovara kodu
        :raises Exception: Ako kod nije validan
        """
        if instruction_code not in OPERATIONS.keys():
            raise Exception(
                f"Error! Invalid instruction code: {instruction_code}")

        return OPERATIONS[instruction_code]

    def is_single_register(self):
        """
        Provjerava da li instrukcija koristi jedan registar.

        :return: True ako koristi tačno jedan registar, inače False
        """
        return self.number_of_registers == 1

    def is_double_register(self):
        """
        Provjerava da li instrukcija koristi dva registra.

        :return: True ako koristi tačno dva registra, inače False
        """
        return self.number_of_registers == 2

    def is_triple_register(self):
        """
        Provjerava da li instrukcija koristi tri registra.

        :return: True ako koristi tačno tri registra, inače False
        """
        return self.number_of_registers == 3

    def __repr__(self):
        """
        Tekstualna reprezentacija operacije.

        :return: Ime instrukcije
        """
        return f"{self.name}"


OPERATIONS = {
    "000000": Operation(
        name="mov",
        registers=["RZ", "RX"],
        type="00",
        operation_code="0000"
    ),
    "000001": Operation(
        name="add",
        registers=["RZ", "RX", "RY"],
        type="00",
        operation_code="0001"
    ),
    "000010": Operation(
        name="sub",
        registers=["RZ", "RX", "RY"],
        type="00",
        operation_code="0010"
    ),
    "000011": Operation(
        name="and",
        registers=["RZ", "RX", "RY"],
        type="00",
        operation_code="0011"
    ),
    "000100": Operation(
        name="or",
        registers=["RZ", "RX", "RY"],
        type="00",
        operation_code="0100"
    ),
    "000101": Operation(
        name="not",
        registers=["RZ", "RX"],
        type="00",
        operation_code="0101"
    ),
    "000110": Operation(
        name="inc",
        registers=["RZ", "RX"],
        type="00",
        operation_code="0110"
    ),
    "000111": Operation(
        name="dec",
        registers=["RZ", "RX"],
        type="00",
        operation_code="0111"
    ),
    "001000": Operation(
        name="shl",
        registers=["RZ", "RX"],
        type="00",
        operation_code="1000"
    ),
    "001001": Operation(
        name="shr",
        registers=["RZ", "RX"],
        type="00",
        operation_code="1001"
    ),
    "001010": Operation(
        name="ashl",
        registers=["RZ", "RX"],
        type="00",
        operation_code="1010"
    ),
    "001011": Operation(
        name="ashr",
        registers=["RZ", "RX"],
        type="00",
        operation_code="1011"
    ),
    "100000": Operation(
        name="ld",
        registers=["RZ", "RY"],
        type="10",
        operation_code="0000"
    ),
    "110000": Operation(
        name="st",
        registers=["RX", "RY"],
        type="11",
        operation_code="0000"
    ),
    "010000": Operation(
        name="jmp",
        registers=[],
        type="01",
        operation_code="0000"
    ),
    "010001": Operation(
        name="jmpz",
        registers=[],
        type="01",
        operation_code="0001"
    ),
    "010010": Operation(
        name="jmps",
        registers=[],
        type="01",
        operation_code="0010"
    ),
    "010011": Operation(
        name="jmpc",
        registers=[],
        type="01",
        operation_code="0011"
    ),
    "010101": Operation(
        name="jmpnz",
        registers=[],
        type="01",
        operation_code="0101"
    ),
    "010110": Operation(
        name="jmpns",
        registers=[],
        type="01",
        operation_code="0110"
    ),
    "010111": Operation(
        name="jmpnc",
        registers=[],
        type="01",
        operation_code="0111"
    )
}
