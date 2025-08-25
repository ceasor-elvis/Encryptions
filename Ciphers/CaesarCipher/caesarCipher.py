class CaesarCipher:
    """
    Encrypt and decrypt text using the Caesar cipher method.

    Example:
        >>> cipher = CaesarCipher("Hello world!", 10)
        >>> encrypted = cipher.encrypt()
        >>> print(encrypted)
        rovvy gybvn!
        >>> decrypted = CaesarCipher(encrypted, 10).decrypt()
        >>> print(decrypted)
        hello world!
    """

    def __init__(self, text: str, shift: int) -> None:
        """
        Initialize the CaesarCipher.

        Args:
            text (str): The text to be encrypted or decrypted.
            shift (int): The number of positions to shift each letter.
        """
        self.text = text.lower()
        self.shift = shift % 26
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'

    def _shift_letter(self, letter: str, shift: int) -> str:
        """
        Shift a single letter by the specified number of positions in the alphabet.

        Args:
            letter (str): The letter to be shifted.
            shift (int): The number of positions to shift the letter.

        Returns:
            str: The shifted letter if it's in the alphabet, otherwise the original character.
        """
        if letter not in self.alphabet:
            return letter
        index = (self.alphabet.index(letter) + shift) % 26
        return self.alphabet[index]

    def encrypt(self) -> str:
        """Encrypt the text using the Caesar cipher."""
        return ''.join(self._shift_letter(char, self.shift) for char in self.text)

    def decrypt(self) -> str:
        """Decrypt the text using the Caesar cipher."""
        return ''.join(self._shift_letter(char, -self.shift) for char in self.text)