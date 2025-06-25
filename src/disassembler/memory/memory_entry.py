class MemoryEntry:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def from_raw_value(raw_value):
        value = MemoryEntry.parse_raw_value(raw_value)
        return MemoryEntry(value=value)

    @staticmethod
    def parse_raw_value(raw_value):
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
        decimal_value = MemoryEntry.convert_hex_to_decimal(hex_value)
        binary_value = MemoryEntry.convert_decimal_to_binary(
            decimal_value,
        )

        return binary_value.zfill(16)

    @staticmethod
    def convert_hex_to_decimal(hex_value):
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
        binary_value = ""

        while decimal_value > 0:
            binary_value += str(decimal_value % 2)
            decimal_value = decimal_value // 2

        return binary_value[::-1]

    @staticmethod
    def convert_binary_to_decimal(binary_value):
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
        bits = map(lambda bit: "1" if bit == "0" else "0", list(binary_value))
        return "".join(list(bits))

    def __repr__(self):
        return f"{self.value}"
