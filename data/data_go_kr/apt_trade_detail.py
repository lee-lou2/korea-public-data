from korea_public_data.core.choices import ResponseType
from korea_public_data.core.vars import default as var
from korea_public_data.core.consts import data as const
from korea_public_data.data.base import PublicDataBase


class GetRTMSDataSvcAptTradeDev(PublicDataBase):
    """국토교통부_아파트매매 실거래 상세 자료"""
    def __init__(self, service_key: str):
        # 상위 클래스 변수 적용
        super().__init__()
        # 필수 설정
        self.service_key = service_key
        # 변수(기본 값 적용)
        self.location_code = var.DEFAULT_APT_TRADE_LOCATION_CODE
        self.yesterday = var.DEFAULT_YESTERDAY_SEOUL_TIMEZONE
        self.search_date = self.yesterday.strftime("%Y%m")
        self.page_no = var.DEFAULT_PAGE_NO
        self.num_of_rows = var.DEFAULT_PAGE_NUM_OF_ROWS
        # 상수
        self.response_type = ResponseType.XML

    @property
    def url(self):
        return (
            f'{const.APT_TRADE_DEV_URL}'
            f'LAWD_CD={self.location_code}&'
            f'DEAL_YMD={self.search_date}&'
            f'pageNo={self.page_no}&'
            f'numOfRows={self.num_of_rows}&'
            f'serviceKey={self.service_key}'
        )

    def _data_valid(self):
        """데이터 이상여부 확인"""
        assert self.service_key, "서비스 키가 등록되지 않았습니다."
