from enum import Enum

class ControlCharacters(Enum):
    LINE_FEED = b'\x0a'
    CARRIAGE_RETURN = b'\x0d'
    SPACE = b'\x20'

class EnglishCharacters(Enum):
    DIGIT_ZERO = b'\x30'
    DIGIT_ONE = b'\x31'
    DIGIT_TWO = b'\x32'
    DIGIT_THREE = b'\x33'
    DIGIT_FOUR = b'\x34'
    DIGIT_FIVE = b'\x35'
    DIGIT_SIX = b'\x36'
    DIGIT_SEVEN = b'\x37'
    DIGIT_EIGHT = b'\x38'
    DIGIT_NINE = b'\x39'
    LATIN_CAPITAL_LETTER_A = b'\x41'
    LATIN_CAPITAL_LETTER_B = b'\x42'
    LATIN_CAPITAL_LETTER_C = b'\x43'
    LATIN_CAPITAL_LETTER_D = b'\x44'
    LATIN_CAPITAL_LETTER_E = b'\x45'
    LATIN_CAPITAL_LETTER_F = b'\x46'
    LATIN_CAPITAL_LETTER_G = b'\x47'
    LATIN_CAPITAL_LETTER_H = b'\x48'
    LATIN_CAPITAL_LETTER_I = b'\x49'
    LATIN_CAPITAL_LETTER_J = b'\x4a'
    LATIN_CAPITAL_LETTER_K = b'\x4b'
    LATIN_CAPITAL_LETTER_L = b'\x4c'
    LATIN_CAPITAL_LETTER_M = b'\x4d'
    LATIN_CAPITAL_LETTER_N = b'\x4e'
    LATIN_CAPITAL_LETTER_O = b'\x4f'
    LATIN_CAPITAL_LETTER_P = b'\x50'
    LATIN_CAPITAL_LETTER_Q = b'\x51'
    LATIN_CAPITAL_LETTER_R = b'\x52'
    LATIN_CAPITAL_LETTER_S = b'\x53'
    LATIN_CAPITAL_LETTER_T = b'\x54'
    LATIN_CAPITAL_LETTER_U = b'\x55'
    LATIN_CAPITAL_LETTER_V = b'\x56'
    LATIN_CAPITAL_LETTER_W = b'\x57'
    LATIN_CAPITAL_LETTER_X = b'\x58'
    LATIN_CAPITAL_LETTER_Y = b'\x59'
    LATIN_CAPITAL_LETTER_Z = b'\x5a'
    LATIN_SMALL_LETTER_A = b'\x61'
    LATIN_SMALL_LETTER_B = b'\x62'
    LATIN_SMALL_LETTER_C = b'\x63'
    LATIN_SMALL_LETTER_D = b'\x64'
    LATIN_SMALL_LETTER_E = b'\x65'
    LATIN_SMALL_LETTER_F = b'\x66'
    LATIN_SMALL_LETTER_G = b'\x67'
    LATIN_SMALL_LETTER_H = b'\x68'
    LATIN_SMALL_LETTER_I = b'\x69'
    LATIN_SMALL_LETTER_J = b'\x6a'
    LATIN_SMALL_LETTER_K = b'\x6b'
    LATIN_SMALL_LETTER_L = b'\x6c'
    LATIN_SMALL_LETTER_M = b'\x6d'
    LATIN_SMALL_LETTER_N = b'\x6e'
    LATIN_SMALL_LETTER_O = b'\x6f'
    LATIN_SMALL_LETTER_P = b'\x70'
    LATIN_SMALL_LETTER_Q = b'\x71'
    LATIN_SMALL_LETTER_R = b'\x72'
    LATIN_SMALL_LETTER_S = b'\x73'
    LATIN_SMALL_LETTER_T = b'\x74'
    LATIN_SMALL_LETTER_U = b'\x75'
    LATIN_SMALL_LETTER_V = b'\x76'
    LATIN_SMALL_LETTER_W = b'\x77'
    LATIN_SMALL_LETTER_X = b'\x78'
    LATIN_SMALL_LETTER_Y = b'\x79'
    LATIN_SMALL_LETTER_Z = b'\x7a'

class EnglishSpecials(Enum):
    EXCLAMATION_MARK = b'\x21'
    QUOTATION_MARK = b'\x22'
    APOSTROPHE = b'\x27'
    LEFT_PARENTHESIS = b'\x28'
    RIGHT_PARENTHESIS = b'\x29'
    ASTERISK = b'\x2a'
    COMMA = b'\x2c'
    HYPHEN_MINUS = b'\x2d'
    FULL_STOP = b'\x2e'
    SOLIDUS = b'\x2f'
    COLON = b'\x3a'
    SEMICOLON = b'\x3b'
    LEFT_SQUARE_BRACKET = b'\x5b'
    RIGHT_SQUARE_BRACKET = b'\x5d'
    GRAVE_ACCENT = b'\x60'
    LEFT_CURLY_BRACKET = b'\x7b'
    RIGHT_CURLY_BRACKET = b'\x7d'
    TILDE = b'\x7e'

class ArabicSpecials(Enum):
    LEFT_POINTING_DOUBLE_ANGLE_QUOTATION_MARK = b'\xc2\xab'
    RIGHT_POINTING_DOUBLE_ANGLE_QUOTATION_MARK = b'\xc2\xbb'
    ARABIC_COMMA = b'\xd8\x8c'
    ARABIC_SEMICOLON = b'\xd8\x9b'
    ARABIC_QUESTION_MARK = b'\xd8\x9f'
    ARABIC_TATWEEL = b'\xd9\x80'
    RIGHT_TO_LEFT_MARK = b'\xe2\x80\x8f'
    EN_DASH = b'\xe2\x80\x93'

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

class ArabicDiacritics(Enum):
    ARABIC_SHADDA_FATHATAN = b'\xd9\x91\xd9\x8b'
    ARABIC_SHADDA_DAMMATAN = b'\xd9\x91\xd9\x8c'
    ARABIC_SHADDA_KASRATAN = b'\xd9\x91\xd9\x8d'
    ARABIC_SHADDA_FATHA = b'\xd9\x91\xd9\x8e'
    ARABIC_SHADDA_DAMMA = b'\xd9\x91\xd9\x8f'
    ARABIC_SHADDA_KASRA = b'\xd9\x91\xd9\x90'
    ARABIC_SHADDA_SUKUN = b'\xd9\x91\xd9\x92'
    ARABIC_FATHATAN = b'\xd9\x8b'
    ARABIC_DAMMATAN = b'\xd9\x8c'
    ARABIC_KASRATAN = b'\xd9\x8d'
    ARABIC_FATHA = b'\xd9\x8e'
    ARABIC_DAMMA = b'\xd9\x8f'
    ARABIC_KASRA = b'\xd9\x90'
    ARABIC_SHADDA = b'\xd9\x91'
    ARABIC_SUKUN = b'\xd9\x92'

class ArabicCharacters(Enum):
    ARABIC_LETTER_HAMZA = b'\xd8\xa1'
    ARABIC_LETTER_ALEF_WITH_MADDA_ABOVE = b'\xd8\xa2'
    ARABIC_LETTER_ALEF_WITH_HAMZA_ABOVE = b'\xd8\xa3'
    ARABIC_LETTER_WAW_WITH_HAMZA_ABOVE = b'\xd8\xa4'
    ARABIC_LETTER_ALEF_WITH_HAMZA_BELOW = b'\xd8\xa5'
    ARABIC_LETTER_YEH_WITH_HAMZA_ABOVE = b'\xd8\xa6'
    ARABIC_LETTER_ALEF = b'\xd8\xa7'
    ARABIC_LETTER_BEH = b'\xd8\xa8'
    ARABIC_LETTER_TEH_MARBUTA = b'\xd8\xa9'
    ARABIC_LETTER_TEH = b'\xd8\xaa'
    ARABIC_LETTER_THEH = b'\xd8\xab'
    ARABIC_LETTER_JEEM = b'\xd8\xac'
    ARABIC_LETTER_HAH = b'\xd8\xad'
    ARABIC_LETTER_KHAH = b'\xd8\xae'
    ARABIC_LETTER_DAL = b'\xd8\xaf'
    ARABIC_LETTER_THAL = b'\xd8\xb0'
    ARABIC_LETTER_REH = b'\xd8\xb1'
    ARABIC_LETTER_ZAIN = b'\xd8\xb2'
    ARABIC_LETTER_SEEN = b'\xd8\xb3'
    ARABIC_LETTER_SHEEN = b'\xd8\xb4'
    ARABIC_LETTER_SAD = b'\xd8\xb5'
    ARABIC_LETTER_DAD = b'\xd8\xb6'
    ARABIC_LETTER_TAH = b'\xd8\xb7'
    ARABIC_LETTER_ZAH = b'\xd8\xb8'
    ARABIC_LETTER_AIN = b'\xd8\xb9'
    ARABIC_LETTER_GHAIN = b'\xd8\xba'
    ARABIC_LETTER_FEH = b'\xd9\x81'
    ARABIC_LETTER_QAF = b'\xd9\x82'
    ARABIC_LETTER_KAF = b'\xd9\x83'
    ARABIC_LETTER_LAM = b'\xd9\x84'
    ARABIC_LETTER_MEEM = b'\xd9\x85'
    ARABIC_LETTER_NOON = b'\xd9\x86'
    ARABIC_LETTER_HEH = b'\xd9\x87'
    ARABIC_LETTER_WAW = b'\xd9\x88'
    ARABIC_LETTER_ALEF_MAKSURA = b'\xd9\x89'
    ARABIC_LETTER_YEH = b'\xd9\x8a'