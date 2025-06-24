from ..constants import EXPECTED_REGISTER_IDENTIFIER_LEN


class Register:
    """
    Predstavlja registar procesora, identifikovan binarnim stringom.

    Omogućava validaciju i parsiranje binarnog identifikatora registra u decimalni broj.
    """

    def __init__(self, raw_register_identifier: str):
        """
        Kreira instancu registra na osnovu binarnog identifikatora.

        :param raw_register_identifier: Binarni string koji identifikuje registar (npr. "001")
        :raises Exception: Ako identifikator nije validan (neispravan format ili dužina)
        """
        if not Register.is_valid_register_identifier(raw_register_identifier):
            raise Exception(
                f"Error! Invalid register identifier: {raw_register_identifier}"
            )

        self.register_number = Register.parse_raw_identifier(
            raw_register_identifier)

    @staticmethod
    def is_valid_register_identifier(raw_register_identifier: str) -> bool:
        """
        Proverava da li je dati string validan binarni identifikator registra.

        :param raw_register_identifier: Binarni string
        :return: True ako je validan, False ako nije
        """
        def is_valid_binary_value(raw_register_identifier: str) -> bool:
            return all(bit in "01" for bit in raw_register_identifier)

        return (
            is_valid_binary_value(raw_register_identifier) and
            len(raw_register_identifier) == EXPECTED_REGISTER_IDENTIFIER_LEN
        )

    @staticmethod
    def parse_raw_identifier(raw_register_identifier: str) -> int:
        """
        Parsira binarni string u decimalni broj registra.

        :param raw_register_identifier: Binarni string
        :return: Decimalni broj registra
        """
        length = len(raw_register_identifier) - 1
        index = length
        register_number = 0

        while index >= 0:
            bit = int(raw_register_identifier[index])
            register_number += pow(2, length - index) * bit
            index -= 1

        return register_number

    def __repr__(self) -> str:
        """
        Vraća tekstualnu reprezentaciju registra u formatu 'R<broj>'.

        :return: String npr. "R3"
        """
        return f"R{self.register_number}"
