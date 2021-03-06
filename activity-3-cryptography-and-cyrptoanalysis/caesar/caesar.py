"""
    Activity 3: Cryptography and Cryptonanalysis
    --------------------------------------------
    Course: Computer and Information Security
    Professor: Jorge Rodríguez Ruiz
    Team:
        Daniela Vignau León (A01021698)
        Carlos García González (A01025948)
        Héctor Alexis Reyes Manrique (A01339607)
"""


alphabet = "abcdefghijklmnopqrstuvwxyz "
length = len(alphabet)


def caesar_cypher(message, key, mode):
    """
    Runs the Caesar encryption algorithm given an input message and a key. If the mode is "enc", it returns an encrypted message. If the mode is "dec", it returns a decrypted one.

    Parameters
    ----------
    message : str
    key: int
    mode: str

    Returns
    -------
    str
    """
    encrypted = ""
    if mode == "dec":
        key = -key
    for l in message:
        index = alphabet.find(l)
        if index != -1:
            index += key
            if index >= length:
                index -= length
            elif index < 0:
                index += length
            encrypted += alphabet[index]
        else:
            print(
                "The character ",
                l,
                " does not exist in the alphabet, it will be left exactly the same",
            )
            encrypted += index
    return encrypted


def main():
    mode = input("Enter 'enc' or 'dec' to encrypt or decrypt the text: ")
    shift = int(input("Enter the shift (int): "))
    if mode == "enc":
        text = input("Enter the text to encrypt: ")
    elif mode == "dec":
        text = input("Enter the text to decrypt: ")
    print(caesar_cypher(text, shift, mode))


if __name__ == "__main__":
    main()
