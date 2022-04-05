from korea_public_data.core.choices import ResponseType
from korea_public_data.core.vars import default as var
from korea_public_data.core.consts import data as const
from korea_public_data.data.base import PublicDataBase


class ExchangeJSON(PublicDataBase):
    """현재 환율 API"""
    def __init__(self, auth_key: str):
        # 상위 클래스 변수 적용
        super().__init__()
        # 필수 설정
        self.auth_key = auth_key
        # 변수(기본 값 적용)
        self.yesterday = var.DEFAULT_TODAY_SEOUL_TIMEZONE
        self.search_date = self.yesterday.strftime("%Y%m%d")
        # 상수
        self.response_type = ResponseType.JSON

    @property
    def url(self):
        return (
            f'{const.BANKING_EXCHANGE_URL}'
            f'authkey={self.auth_key}&'
            f'searchdate={self.search_date}&'
            f'data=AP01'
        )

    def _data_valid(self):
        """데이터 이상여부 확인"""
        assert self.auth_key, "서비스 키가 등록되지 않았습니다."
