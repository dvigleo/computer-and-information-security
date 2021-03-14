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
from collections import Counter
import json

parser = argparse.ArgumentParser()
parser.add_argument("file", type=str)
args = parser.parse_args()

f_in = open(args.file, "r")
input_message = f_in.read()

key_length = 4

counts = []

for i in range(key_length):
    position = []
    for j in range(i, len(input_message), key_length):
        position.append(input_message[j])
    count = Counter(position)
    print(count)
    counts.append(count)

f_out = open("data.json", "w")
json.dump(counts, f_out)
