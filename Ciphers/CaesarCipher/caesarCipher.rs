pub struct CaesarCipher {
    text: String,
    shift: u8,
}

impl CaesarCipher {
    /// Initialize the CaesarCipher.
    pub fn new(text: &str, shift: u8) -> Self {
        CaesarCipher {
            text: text.to_lowercase(),
            shift: shift % 26,
        }
    }

    /// Shift a single letter by the specified number of positions in the alphabet.
    fn shift_letter(letter: char, shift: i8) -> char {
        if !letter.is_ascii_alphabetic() {
            return letter;
        }

        let base = b'a';
        let offset = letter as i8 - base as i8;
        // rem_euclid correctly handles negative numbers for decryption
        let new_offset = (offset + shift).rem_euclid(26);
        
        (base + new_offset as u8) as char
    }

    /// Encrypt the text using the Caesar cipher.
    pub fn encrypt(&self) -> String {
        self.text
            .chars()
            .map(|c| Self::shift_letter(c, self.shift as i8))
            .collect()
    }

    /// Decrypt the text using the Caesar cipher.
    pub fn decrypt(&self) -> String {
        self.text
            .chars()
            .map(|c| Self::shift_letter(c, -(self.shift as i8)))
            .collect()
    }
}

fn main() {
    let cipher = CaesarCipher::new("Hello world!", 10);
    let encrypted = cipher.encrypt();
    println!("Encrypted: {}", encrypted); // rovvy gybvn!
    
    let decrypted = CaesarCipher::new(&encrypted, 10).decrypt();
    println!("Decrypted: {}", decrypted); // hello world!
}
