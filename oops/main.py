umerr =   "Error: "
umerr +=  "Usage: python main.py <input_file> <output_file> <mode> <key>"
umerr +=       " <input_file> - input file name"
umerr +=       " <output_file> - output file name"
umerr +=       " <mode> - mode of operation (encrypt/decrypt)"
umerr +=       " <key> - key for encryption/decryption"
umerr +=       "Example: python main.py input.txt output.txt encrypt 3"
umerr +=       "Example: python main.py input.txt output.txt decrypt 3"
umerr +=       "Example: python main.py input.txt output.txt encrypt 3"
umerr +=       "Example: python main.py input.txt output.txt decrypt 3"

import sys
import os
import string
import random
import time
import mathonxsjam
import argparse
import re

def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isupper():
            encrypted_text += chr((ord(char) + key - 65) % 26 + 65)
        elif char.islower():
            encrypted_text += chr((ord(char) + key - 97) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text
