class CeasarCipher:
    """Encrypt a text using the ceasor cipher method."""
    def __init__(self, text:str, encryp_number:int) -> None:
        """
        Arguments
        - text: str -> The text to be encrpyted.
        - encryp_number: int -> The number of letters to skip and replace with the original one. The number can reach a certain threshold and throw an error
        , so it is is mindful to use a number not exceeding the characters in the alphabet in other words (26)

        The program just deals alpha letters and not any special character.
        Special characters given in the text input will be ignored and returned in the output text
        ### Example:
        ```python
        print(CeasarCipher("Hello world!", 10).encrypt())
        print(CeasarCipher("rovvy gybvn!", 10).decrypt())
        ```
        """
        self.text = text.lower()
        self.encryption_number = encryp_number
        self.lower_case = list("abcdefghijklmnopqrstuvwxyz")
        self.list_text =  list(self.text)

    def encrypt(self) -> str:
        """Returns the encrpypted text"""
        text = []
        for letter in self.list_text:
            if letter not in self.lower_case:
                text.append(letter)
            else:
                l_index = self.lower_case.index(letter) + self.encryption_number
                if l_index > len(self.lower_case)-1:
                    l_index = l_index%len(self.lower_case)
                
                text.append(self.lower_case[l_index])
        return str().join(text)
    
    def decrypt(self) -> str:
        """Returns the decrypted text given the encrpytion number is the same as the one used to encrypt it."""
        text = []
        for letter in self.list_text:
            if letter not in self.lower_case:
                text.append(letter)
            else:
                l_index = self.lower_case.index(letter) - self.encryption_number
                if l_index < 0:
                    l_index = len(self.lower_case) + l_index
                text.append(self.lower_case[l_index])
        
        return str().join(text)