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


import argparse

alphabet = "abcdefghijklmnopqrstuvwxyz "


def vigenere(input_message, key, method):
    """
    Runs the Vigenere encryption algorithm given an input message and a key. If the method is "encode", it returns an encrypted message. If the method is "decode", it returns a decrypted one.

    Parameters
    ----------
    input_message : str
    key: str
    method: str

    Returns
    -------
    str
    """
    output_message = ""
    index = 0
    for c in input_message:
        if index == len(key):
            index = 0
        x = alphabet.find(c)
        y = alphabet.find(key[index])
        if method == "encode":
            result = x + y
        elif method == "decode":
            result = x - y
        mod = result % len(alphabet)
        output_message += alphabet[mod]
        index += 1
    return output_message


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=str)
    parser.add_argument("-k", "--key", type=str)
    parser.add_argument("-m", "--method", type=str)
    args = parser.parse_args()

    f_in = open(args.file, "r")

    input_message = f_in.read()
    key = args.key
    method = args.method

    output_text = vigenere(input_message, key, method)

    f_out = open("output-message.txt", "w")
    f_out.write(output_text)

