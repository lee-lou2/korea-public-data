from korea_public_data.core.choices import ResponseType
from korea_public_data.core.vars import default as var
from korea_public_data.core.consts import data as const
from korea_public_data.data.base import PublicDataBase


class GetCovid19InfStateJson(PublicDataBase):
    """공공데이터활용지원센터_보건복지부 코로나19 감염 현황"""
    def __init__(self, service_key: str):
        # 상위 클래스 변수 적용
        super().__init__()
        # 필수 설정
        self.service_key = service_key
        # 변수(기본 값 적용)
        self.yesterday = var.DEFAULT_YESTERDAY_SEOUL_TIMEZONE
        self.start_at = self.yesterday.strftime("%Y%m%d")
        self.end_at = self.yesterday.strftime("%Y%m%d")
        self.page_no = var.DEFAULT_PAGE_NO
        self.num_of_rows = var.DEFAULT_PAGE_NUM_OF_ROWS
        # 상수
        self.response_type = ResponseType.XML

    @property
    def url(self):
        return (
            f'{const.COVID_INFECTION_STATUS_URL}'
            f'startCreateDt={self.start_at}&'
            f'endCreateDt={self.end_at}&'
            f'pageNo={self.page_no}&'
            f'numOfRows={self.num_of_rows}&'
            f'serviceKey={self.service_key}'
        )

    def _data_valid(self):
        """데이터 이상여부 확인"""
        assert self.service_key, "서비스 키가 등록되지 않았습니다."
