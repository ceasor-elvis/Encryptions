# Encryptions

A repository that contains examples of simple encryptions.

## Overview

This project aims to demonstrate various simple encryption techniques. It serves as an educational resource for those interested in understanding basic cryptographic concepts and their implementations.

## Table of Contents

- [Installation](#installation)
- [Requirements](#requirements)
- [Usage](#usage)
- [Encryption Methods](#encryption-methods)
- [Contributing](#contributing)


## Installation

To use this project, clone the repository to your local machine:

```bash
git clone https://github.com/ceasor-elvis/Encryptions.git
cd Encryptions
```

## Requirements

- Python 3.x (for the Python-based implementation)
- Node.js (for the JavaScript-based implementation)

## Usage

### Python
```python
cipher = CaesarCipher("Hello world!", 10)

# Encrypted text
encrypted = cipher.encrypt()
print(encrypted) # rovvy gybvn!

# Decrypted text
decrypted = CaesarCipher(encrypted, 10).decrypt()
print(decrypted) # hello world!
```

### JavaScript
```javascript
const cipher = new CaesarCipher("Hello world!", 10);

// Encrypted text
const encrypted = cipher.encrypt();
console.log(encrypted); // rovvy gybvn!

// Decrypted text
const decrypted = new CaesarCipher(encrypted, 10).decrypt();
console.log(decrypted); // hello world!
```