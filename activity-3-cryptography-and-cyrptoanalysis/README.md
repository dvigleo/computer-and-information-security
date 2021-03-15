# Cryptoanalysis and Cryptography

---

#### Team members

- [Daniela Vignau (A01021698)](https://github.com/dvigleo)
- [Héctor Reyes (A01339607)](https://github.com/hreyesm)
- [Carlos García (A01025948)](https://github.com/cxrlos)

## Decryption of Cipher1 with Caesar Encoding

A brute force approach was used in order to find the shift to decrypt the [cipher1.txt](./caesar/cipher1.txt) file. The shift that was used to encrypt it was **10**. See [cipher1-decrypted.txt](./caesar/cipher1-decrypted.txt) for the decrypted text.

## Decryption of Cipher2 with Vigeneres Encoding

A statistical analysis was done using the [helper.py](./vigenere/helper.py) script, which counts the number of occurrences in each of the four positions of the four-character key. With this approach in mind, it was determined that the most frequent characters from the alphabet in each position were as follows:

- First position: "g"
- Second position: " "
- Third position: "b"
- Fourth position: "j"

After gathering this information, it came up to the team that the most frequent character of any text in the English language is the whitespace character (" "). This made the team realize that, if each of the above characters are shifted one slot to the right, the word "hack" is revealed. Thus, the key that was used to encrypt the [cipher2.txt](./vigenere/cipher2.txt) file was **hack**. See [cipher2-decrypted.txt](./vigenere/cipher2-decrypted.txt) for the decrypted text.
