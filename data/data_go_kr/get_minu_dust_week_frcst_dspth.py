from korea_public_data.core.choices import ResponseType
from korea_public_data.core.vars import default as var
from korea_public_data.core.consts import data as const
from korea_public_data.data.base import PublicDataBase


class GetMinuDustWeekFrcstDspth(PublicDataBase):
    """한국환경공단_에어코리아_대기오염정보"""
    def __init__(self, service_key: str):
        # 상위 클래스 변수 적용
        super().__init__()
        # 필수 설정
        self.service_key = service_key
        # 변수(기본 값 적용)
        self.now = var.DEFAULT_TODAY_SEOUL_TIMEZONE
        self.search_date = self.now.strftime("%Y-%m-%d")
        self.page_no = var.DEFAULT_PAGE_NO
        self.num_of_rows = var.DEFAULT_PAGE_NUM_OF_ROWS
        # 상수
        self.response_type = ResponseType.XML

    @property
    def url(self):
        return (
            f'{const.MINU_DUST_WEEK_FRCST_DSPTH_URL}'
            f'returnType=xml&'
            f'pageNo={self.page_no}&'
            f'numOfRows={self.num_of_rows}&'
            f'searchDate={self.search_date}&'
            f'serviceKey={self.service_key}'
        )

    def _data_valid(self):
        """데이터 이상여부 확인"""
        assert self.service_key, "서비스 키가 등록되지 않았습니다."
