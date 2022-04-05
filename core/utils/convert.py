import re
from hangul_utils import split_syllables
from korea_public_data.core.consts.util import KOR_ENG_TABLE


def dict_to_str(data: dict) -> str:
    """딕셔너리를 모두 연결"""
    return "".join([f"{key}{value}" for key, value in data.items()])


def kor_text_to_id(kor_text: str) -> str:
    """일반 텍스트를 id로 변환"""
    sub_kor_text = re.sub('[^A-Za-z0-9가-힣]', '', kor_text).strip()
    split_text = split_syllables(sub_kor_text)
    return ''.join(
        [
            word.replace(word, KOR_ENG_TABLE[word])
            if KOR_ENG_TABLE.get(word) else word
            for word in str(split_text)
        ]
    )
