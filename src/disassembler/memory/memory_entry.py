class MemoryEntry:
    """
    Predstavlja memorijsku vrijednost dekodiranu iz heksadecimalnog oblika
    kao potpisani cijeli broj (signed integer).
    """

    def __init__(self, value):
        """
        Inicijalizuje instancu klase sa zadatom vrijednošću.

        :param value: Potpisana cijela vrijednost memorijskog zapisa.
        """
        self.value = value

    @staticmethod
    def from_raw_value(raw_value):
        """
        Kreira instancu klase MemoryEntry iz heksadecimalnog stringa.

        :param raw_value: Heksadecimalni string.
        :return: Instanca klase MemoryEntry.
        """
        value = MemoryEntry.parse_raw_value(raw_value)
        return MemoryEntry(value=value)

    @staticmethod
    def parse_raw_value(raw_value):
        """
        Parsira heksadecimalni string i vraća njegovu potpisanu cijelu vrijednost.
        Pretpostavlja se da je broj u komplement 2 obliku (16-bitni).

        :param raw_value: Heksadecimalni string.
        :return: Potpisana cijela vrijednost.
        :raises Exception: Ako je unos prazan ili neispravan.
        """
        if not raw_value:
            raise Exception(
                f"Error! Invalid memory entry."
            )

        binary_value = MemoryEntry.convert_hex_to_binary(raw_value)

        if binary_value[0] == "1":
            # If the MSB is 1 we need to use the
            # two's complement of the binary number.

            binary_value = MemoryEntry.invert_binary_value(binary_value)
            decimal_value = MemoryEntry.convert_binary_to_decimal(binary_value)
            decimal_value += 1
            return -1 * decimal_value

        return MemoryEntry.convert_binary_to_decimal(binary_value)

    @staticmethod
    def convert_hex_to_binary(hex_value):
        """
        Pretvara heksadecimalni string u binarni string dužine 16 bita.

        :param hex_value: Heksadecimalni string.
        :return: Binarni string (16 bita).
        """
        decimal_value = MemoryEntry.convert_hex_to_decimal(hex_value)
        binary_value = MemoryEntry.convert_decimal_to_binary(
            decimal_value,
        )

        return binary_value.zfill(16)

    @staticmethod
    def convert_hex_to_decimal(hex_value):
        """
        Pretvara heksadecimalni string u decimalni broj.

        :param hex_value: Heksadecimalni string.
        :return: Decimalna vrijednost.
        """
        last_index = len(hex_value) - 1
        index = last_index
        decimal_value = 0

        while index >= 0:
            bit = MemoryEntry.convert_hex_digit_to_decimal_digit(
                hex_value[index]
            )
            decimal_value += pow(16, last_index - index) * bit
            index -= 1

        return decimal_value

    @staticmethod
    def convert_hex_digit_to_decimal_digit(hex_digit):
        """
        Pretvara heksadecimalnu cifru u decimalnu cifru.

        :param hex_digit: Karakter (0-9, A-F).
        :return: Decimalna cifra.
        :raises Exception: Ako je cifra neispravna.
        """
        ALLOWED_DIGITS = [
            "0", "1", "2", "3", "4", "5", "6",
            "7", "8", "9", "A", "B", "C", "D",
            "E", "F"
        ]

        if not hex_digit or hex_digit.upper() not in ALLOWED_DIGITS:
            raise Exception(
                f"Error! Invalid hex digit in memory entry: ${hex_digit}"
            )

        hex_digit = hex_digit.upper()
        return int(hex_digit) if hex_digit.isnumeric() else ord(hex_digit) - 55

    @staticmethod
    def convert_decimal_to_binary(decimal_value):
        """
        Pretvara decimalni broj u binarni string.

        :param decimal_value: Decimalni broj.
        :return: Binarni string.
        """
        binary_value = ""

        while decimal_value > 0:
            binary_value += str(decimal_value % 2)
            decimal_value = decimal_value // 2

        return binary_value[::-1]

    @staticmethod
    def convert_binary_to_decimal(binary_value):
        """
        Pretvara binarni string u decimalni broj.

        :param binary_value: Binarni string.
        :return: Decimalna vrijednost.
        """
        last_index = len(binary_value) - 1
        index = last_index
        decimal_value = 0

        while index >= 0:
            bit = int(binary_value[index])
            decimal_value += pow(2, last_index - index) * bit
            index -= 1

        return decimal_value

    @staticmethod
    def invert_binary_value(binary_value):
        """
        Invertuje svaki bit binarnog stringa (koristi se za komplement 2).

        :param binary_value: Binarni string.
        :return: Inverzija binarnog stringa.
        """
        bits = map(lambda bit: "1" if bit == "0" else "0", list(binary_value))
        return "".join(list(bits))

    def __repr__(self):
        return f"{self.value}"
