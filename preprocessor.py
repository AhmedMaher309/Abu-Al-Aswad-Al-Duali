import os

from enum import Enum
import re
import numpy as np
from pyarabic.araby import tokenize, is_arabicrange, strip_tashkeel

from file_reader import FileReader


class ArabicDiacritics(Enum):
    FATHATAN = '\u064b'
    DAMMATAN = '\u064c'
    KASRATAN = '\u064d'
    FATHA = '\u064e'
    DAMMA = '\u064f'
    KASRA = '\u0650'
    SHADDA = '\u0651'
    SUKUN = '\u0652'

class Preprocessor:

    def __init__(self):
        f = FileReader()


    # clean the arabic text from any non arabic characters and store the clean data inside an new output file
    def clean_data(self, data,output_file):
        tokens = tokenize(data, conditions=is_arabicrange)
        cleaned_data = u" ".join(tokens)
        f.write_file(output_file, cleaned_data)

    # remove diacritics from arabic text and store the new data inside a new file
    def remove_diacritics(self, data, output_file):
        data_with_diactrics = strip_tashkeel(data)
        f.write_file(output_file, data_with_diactrics)

    # remove all punctuation characters and store the result inside the output file
    def remove_tarkeem(self, data, output_file):
        arabic_punctuation = ['،', '٪', '؛', '؟', 'ـ']
        english_punctuation = [',', '.', '%', ':', ';', '?', '!', '-', '_', "'", '"', '(', ')', '[', ']', '{', '}']
        data_without_tarkeem = ""
        for character in data:
            if character not in arabic_punctuation and character not in english_punctuation:
                data_without_tarkeem += character
        f.write_file(output_file, data_without_tarkeem)

    def separate_diacritics(self, arabic_text):
        diacritics_list = []
        # internal function to replace diacritics with empty strings for the letters
        def diacritics_replacement(match):
            diacritic = match.group(0)
            diacritics_list.append(diacritic)
            return ''  
        
        # Define a pattern to match Arabic diacritics and shadda using the enum values
        diacritics_pattern = re.compile("|".join([re.escape(diacritic.value) for diacritic in ArabicDiacritics]))

        # Remove diacritics and shadda using the pattern and store them in the list
        result_text = diacritics_pattern.sub(diacritics_replacement, arabic_text)

        return result_text, diacritics_list
    
    