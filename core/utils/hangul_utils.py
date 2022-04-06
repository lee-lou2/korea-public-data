# ----------------
# 한글을 자음/모음 분리
# ----------------
INITIALS = list(map(lambda x: chr(x), [
    0x3131, 0x3132, 0x3134, 0x3137, 0x3138, 0x3139, 0x3141, 0x3142, 0x3143, 0x3145,
    0x3146, 0x3147, 0x3148, 0x3149, 0x314a, 0x314b, 0x314c, 0x314d, 0x314e
]))
MEDIALS = list(map(lambda x: chr(x), [
    0x314f, 0x3150, 0x3151, 0x3152, 0x3153, 0x3154, 0x3155, 0x3156, 0x3157, 0x3158,
    0x3159, 0x315a, 0x315b, 0x315c, 0x315d, 0x315e, 0x315f, 0x3160, 0x3161, 0x3162,
    0x3163
]))
FINALS = list(map(lambda x: chr(x), [
    0x3131, 0x3132, 0x3133, 0x3134, 0x3135, 0x3136, 0x3137, 0x3139, 0x313a, 0x313b,
    0x313c, 0x313d, 0x313e, 0x313f, 0x3140, 0x3141, 0x3142, 0x3144, 0x3145, 0x3146,
    0x3147, 0x3148, 0x314a, 0x314b, 0x314c, 0x314d, 0x314e
]))


def check_syllable(x):
    return 0xAC00 <= ord(x) <= 0xD7A3


def split_syllable_char(x):
    if len(x) != 1:
        raise ValueError("Input string must have exactly one character.")

    if not check_syllable(x):
        raise ValueError("Input string does not contain a valid Korean character.")

    diff = ord(x) - 0xAC00
    _m = diff % 28
    _d = (diff - _m) // 28

    initial_index = _d // 21
    medial_index = _d % 21
    final_index = _m

    if not final_index:
        result = (INITIALS[initial_index], MEDIALS[medial_index])
    else:
        result = (INITIALS[initial_index], MEDIALS[medial_index], FINALS[final_index - 1])

    return result


def split_syllables(string):
    new_string = ""
    for c in string:
        if not check_syllable(c):
            new_c = c
        else:
            new_c = "".join(split_syllable_char(c))
        new_string += new_c

    return new_string


# ----------
# 한글-영어 변환
# ----------
KOR_WORDS = list('ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ')
ENG_WORDS = [
    'r', 'R', 'rt', 's', 'sw', 'sg', 'e', 'f', 'fr', 'fa', 'fq', 'ft',
    'fx', 'fv', 'fg', 'a', 'q', 'qt', 't', 'T', 'd', 'w', 'c', 'z',
    'x', 'v', 'g', 'k', 'o', 'i', 'O', 'j', 'p', 'u', 'P', 'h', 'hk',
    'ho', 'hl', 'y', 'n', 'nj', 'np', 'nl', 'b', 'm', 'ml', 'l'
]
KOR_ENG_TABLE = dict(zip(KOR_WORDS, ENG_WORDS))
