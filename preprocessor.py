import os

from enum import Enum
import re
import numpy as np
from pyarabic.araby import tokenize, is_arabicrange, strip_tashkeel

from file_reader import FileReader


class ArabicDiacritics(Enum):
    SHADDA_FATHATAN = '\u0651\u064b'
    SHADDA_DAMMATAN = '\u0651\u064c'
    SHADDA_KASRATAN = '\u0651\u064d'
    SHADDA_FATHA = '\u0651\u064e'
    SHADDA_DAMMA = '\u0651\u064f'
    SHADDA_KASRA = '\u0651\u0650'
    SHADDA_SUKUN = '\u0651\u0652'
    SHADDA = '\u0651'
    FATHATAN = '\u064b'
    DAMMATAN = '\u064c'
    KASRATAN = '\u064d'
    FATHA = '\u064e'
    DAMMA = '\u064f'
    KASRA = '\u0650'
    SUKUN = '\u0652'

class ArabicCharacters(Enum):
    HAMZA = u'\u0621'
    ALEF_MADDA = u'\u0622'
    ALEF_HAMZA_ABOVE = u'\u0623'
    WAW_HAMZA = u'\u0624'
    ALEF_HAMZA_BELOW = u'\u0625'
    YEH_HAMZA = u'\u0626'
    ALEF = u'\u0627'
    BEH = u'\u0628'
    TEH_MARBUTA = u'\u0629'
    TEH = u'\u062a'
    THEH = u'\u062b'
    JEEM = u'\u062c'
    HAH = u'\u062d'
    KHAH = u'\u062e'
    DAL = u'\u062f'
    THAL = u'\u0630'
    REH = u'\u0631'
    ZAIN = u'\u0632'
    SEEN = u'\u0633'
    SHEEN = u'\u0634'
    SAD = u'\u0635'
    DAD = u'\u0636'
    TAH = u'\u0637'
    ZAH = u'\u0638'
    AIN = u'\u0639'
    GHAIN = u'\u063a'
    TATWEEL = u'\u0640'
    FEH = u'\u0641'
    QAF = u'\u0642'
    KAF = u'\u0643'
    LAM = u'\u0644'
    MEEM = u'\u0645'
    NOON = u'\u0646'
    HEH = u'\u0647'
    WAW = u'\u0648'
    ALEF_MAKSURA = u'\u0649'
    YEH = u'\u064a'

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
            diacritic = match.group(2)
            diacritics_list.append(diacritic)
            return match.group(1) 
        
        # Define a pattern to match Arabic diacritics and shadda using the enum values
        diacritics_pattern = re.compile("([" + "".join([re.escape(character.value) for character in ArabicCharacters]) + " ])" + "([" + "".join([re.escape(diacritic.value) for diacritic in ArabicDiacritics]) + "]*)|(.)")

        # Remove diacritics and shadda using the pattern and store them in the list
        result_text = re.sub(diacritics_pattern, diacritics_replacement, arabic_text)

        return result_text, diacritics_list
