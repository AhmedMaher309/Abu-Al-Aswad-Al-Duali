import os

from enum import Enum
import re
import numpy as np
from pyarabic.araby import tokenize, is_arabicrange, strip_tashkeel

from file_reader import FileReader
from chars_enums import *

class Preprocessor:

    def __init__(self):
        self.f = FileReader()


    # clean the arabic text from any non arabic characters and store the clean data inside an new output file
    def clean_data(self, data):
        tokens = tokenize(data, conditions=is_arabicrange)
        cleaned_data = u" ".join(tokens)
        return cleaned_data

    # remove diacritics from arabic text and store the new data inside a new file
    def remove_diacritics(self, data):
        data_without_diactrics = strip_tashkeel(data)
        return data_without_diactrics


    # remove all punctuation characters and store the result inside the output file
    def remove_tarkeem(self, data):
        arabic_punctuation = ['،', '٪', '؛', '؟', 'ـ']
        english_punctuation = [',', '.', '%', ':', ';', '?', '!', '-', '_', "'", '"', '(', ')', '[', ']', '{', '}']
        data_without_tarkeem = ""
        for character in data:
            if character not in arabic_punctuation and character not in english_punctuation:
                data_without_tarkeem += character
        return data_without_tarkeem
        

    def separate_diacritics(self, arabic_text):
        diacritics_list = []
        # internal function to replace diacritics with empty strings for the letters
        def diacritics_replacement(match):
            diacritic = match.group(2) if match.group(2) is not None else ""
            diacritics_list.append(diacritic)
            return match.group(1) 
        
        # Define a pattern to match Arabic diacritics and shadda using the enum values
        diacritics_pattern = re.compile("([" + "".join([re.escape(character.value.decode("utf-8")) for character in ArabicCharacters]) + " ])" + "([" + "".join([re.escape(diacritic.value.decode("utf-8")) for diacritic in ArabicDiacritics]) + "]*)|(.)")

        # Remove diacritics and shadda using the pattern and store them in the list
        result_text = re.sub(diacritics_pattern, diacritics_replacement, arabic_text)

        return result_text, diacritics_list

    def tokenize_data(self, arabic_text, output_file_tokens, output_file_diacritics_list):
        tokens = tokenize(arabic_text)
        letters_tokens = []
        diacritics_tokens = []
        for token in tokens:
          letters, diacritic = self.separate_diacritics(token)
          letters_tokens.append(letters)
          diacritics_tokens.append(diacritic)

        self.f.write_file_binary(output_file_tokens, letters_tokens )
        self.f.write_file_binary(output_file_diacritics_list, diacritics_tokens )


    def read_tokenized_data(self, file_tokens, file_diacritics_list):
        result_text = self.f.open_file_binary(file_tokens)
        diacritics_list = self.f.open_file_binary(file_diacritics_list)
        return result_text, diacritics_list



