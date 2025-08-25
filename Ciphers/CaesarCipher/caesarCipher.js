// The CaesarCipher class Implemented in JavaScript.

class CaesarCipher {
  /*
    Encrypt and decrypt text using the Caesar cipher method.

    Example:
        >>> let cipher = CaesarCipher("Hello world!", 10)
        >>> let encrypted = cipher.encrypt()
        >>> console.log(encrypted)
            rovvy gybvn!
        >>> let decrypted = CaesarCipher(encrypted, 10).decrypt()
        >>> console.log(decrypted)
            hello world!
    */
  constructor(text, shift) {
    /**
        Initialize the CaesarCipher.
        Args:
            text (str): The text to be encrypted or decrypted.
            shift (int): The number of positions to shift each letter.
     */
    this.text = text.toLowerCase();
    this.shift = shift % 26;
    this.alphabet = "abcdefghijklmnopqrstuvwxyz";
  }

  // Class Methods
  _shift_letter(letter, shift) {
    /*
            Shift a single letter by the specified number of positions in the alphabet.

        Args:
            letter (str): The letter to be shifted.
            shift (int): The number of positions to shift the letter.

        Returns:
            str: The shifted letter if it's in the alphabet, otherwise the original character.
             */
    if (!this.alphabet.includes(letter)) {
      return letter;
    }
    let index = (this.alphabet.indexOf(letter) + shift + 26) % 26;
    return this.alphabet[index];
  }
  encrypt() {
    /* Encrypt the text using the Caesar cipher. */
    let result = "";
    for (let i = 0; i < this.text.length; i++) {
      result += this._shift_letter(this.text[i], this.shift);
    }
    return result;
  }
  decrypt() {
    /* Decrypt the text using the Caesar cipher. */
    let result = "";
    for (let i = 0; i < this.text.length; i++) {
      result += this._shift_letter(this.text[i], -this.shift);
    }
    return result;
  }
}
