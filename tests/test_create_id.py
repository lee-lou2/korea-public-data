from korea_public_data.core.utils.convert import kor_text_to_id, dict_to_str


def test_create_id():
    # 변환 데이터
    dict_values = {
        "지역": "서울",
        "일시": "2022-01-01 10:00",
        "확률": "50%"
    }
    str_value = dict_to_str(dict_values)
    idx = kor_text_to_id(str_value)

    # 검증 데이터
    location = "wldurtjdnf"  # 지역
    datetime = "dlftl202201011000"  # 일시
    percent = "ghkrfbf50"  # 확률
    assert idx == f"{location}{datetime}{percent}"
