class AffineCipher:
    """
    Encrypt and decrypt text using the classic Affine cipher method.

    Example:
        >>> cipher = AffineCipher("Hello world!", 5, 8)
        >>> encrypted = cipher.encrypt()
        >>> print(encrypted)
        rclla oaplx!
        >>> decrypted = AffineCipher(encrypted, 5, 8).decrypt()
        >>> print(decrypted)
        hello world!
    """

    def __init__(self, text: str, a: int = 5, b: int = 8) -> None:
        """
        Initialize the AffineCipher.

        Args:
            text (str): The text to be encrypted or decrypted.
            a (int, optional): The multiplicative key for the cipher. Defaults to 5.
            b (int, optional): The additive key for the cipher. Defaults to 8.
        """
        self.text = text.lower()
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.m = len(self.alphabet)
        self.a = a # Multiplicative key
        self.b = b  # Additive key
        
    def _mod_inverse(self, a: int, m: int) -> int:
        """
        Compute the modular inverse of a under modulo m using the Extended Euclidean Algorithm.

        Args:
            a (int): The number to find the modular inverse for.
            m (int): The modulo.

        Returns:
            int: The modular inverse of a under modulo m.
        """
        m0, x0, x1 = m, 0, 1
        if m == 1:
            return 0
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        if x1 < 0:
            x1 += m0
        return x1

    def _is_a_valid(self) -> bool:
        """
        Checks if the multiplicative key 'a' is valid (i.e., coprime with the length of the alphabet).
        Returns:
            bool: True if 'a' is valid, False otherwise.
        """
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x
        return gcd(self.a, self.m) == 1

    def encrypt(self) -> str:
        """
        Encrypts the input text using the Affine Cipher algorithm.
        The encryption is performed using the formula: E(x) = (a * x + b) mod m,
        where 'a' and 'b' are keys, 'x' is the index of the character in the alphabet,
        and 'm' is the length of the alphabet.
        Non-alphabet characters are left unchanged.
        Raises:
            ValueError: If the multiplicative key 'a' is not coprime with 'm'.
        Returns:
            str: The encrypted text.
        """
        if not self._is_a_valid():
            raise ValueError(f"The multiplicative key 'a'={self.a} is not valid. It must be coprime with {self.m}.")
        
        encrypted_text = []
        for char in self.text:
            if char in self.alphabet:
                x = self.alphabet.index(char)
                encrypted_char = self.alphabet[(self.a * x + self.b) % self.m]
                encrypted_text.append(encrypted_char)
            else:
                encrypted_text.append(char)
        return ''.join(encrypted_text)
    
    def decrypt(self):
        """
        Decrypts the text using the Affine Cipher algorithm.
        The method first checks if the multiplicative key 'a' is valid (coprime with the modulus 'm').
        If valid, it computes the modular inverse of 'a' and applies the Affine Cipher decryption formula
        to each character in the text that exists in the defined alphabet. Characters not in the alphabet
        are left unchanged.
        Returns:
            str: The decrypted text.

        Raises:
            ValueError: If the multiplicative key 'a' is not valid (not coprime with 'm').
        """
        if not self._is_a_valid():
            raise ValueError(f"The multiplicative key 'a'={self.a} is not valid. It must be coprime with {self.m}.")
        a_inv = self._mod_inverse(self.a, self.m)
        decrypted_text = []
        for char in self.text:
            if char in self.alphabet:
                y = self.alphabet.index(char)
                decrypted_char = self.alphabet[(a_inv * (y - self.b)) % self.m]
                decrypted_text.append(decrypted_char)
            else:
                decrypted_text.append(char)
        return ''.join(decrypted_text)