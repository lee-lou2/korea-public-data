from korea_public_data.core.choices import ResponseType
from korea_public_data.core.consts import data as const
from korea_public_data.data.base import PublicDataBase


class SOCityStats(PublicDataBase):
    """여성가족부_성범죄자 지역별 통계"""
    def __init__(self):
        # 상위 클래스 변수 적용
        super().__init__()
        # 상수
        self.response_type = ResponseType.XML

    @property
    def url(self):
        return (
            f'{const.SO_CITY_STATS_URL}'
        )

    def _data_valid(self):
        """데이터 이상여부 확인"""
        pass
