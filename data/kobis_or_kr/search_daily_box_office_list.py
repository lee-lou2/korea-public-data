from korea_public_data.core.choices import ResponseType
from korea_public_data.core.vars import default as var
from korea_public_data.core.consts import data as const
from korea_public_data.data.base import PublicDataBase


class SearchDailyBoxOfficeList(PublicDataBase):
    """일별 박스 오피스 순위"""
    def __init__(self, key: str):
        # 상위 클래스 변수 적용
        super().__init__()
        # 필수 설정
        self.key = key
        # 변수(기본 값 적용)
        self.yesterday = var.DEFAULT_YESTERDAY_SEOUL_TIMEZONE
        self.target_dt = self.yesterday.strftime("%Y%m%d")
        self.item_per_page = var.DEFAULT_ITEM_PER_PAGE
        self.multi_movie_yn = var.DEFAULT_MULTI_MOVIE_YN
        self.rep_nation_cd = var.DEFAULT_REP_NATION_CD
        self.wide_area_cd = var.DEFAULT_WIDE_AREA_CD
        # 상수
        self.response_type = ResponseType.JSON

    @property
    def url(self):
        multi_movie_yn = f'multiMovieYn={self.multi_movie_yn}&' if self.multi_movie_yn else ''
        rep_nation_cd = f'repNationCd={self.rep_nation_cd}&' if self.rep_nation_cd else ''
        wide_area_cd = f'wideAreaCd={self.wide_area_cd}&' if self.wide_area_cd else ''
        return (
            f'{const.SEARCH_DAILY_BOX_OFFICE_LIST_URL}'
            f'key={self.key}&'
            f'targetDt={self.target_dt}&'
            f'{multi_movie_yn}'
            f'{rep_nation_cd}'
            f'{wide_area_cd}'
            f'itemPerPage={self.item_per_page}'
        )

    def _data_valid(self):
        """데이터 이상여부 확인"""
        assert self.key, "서비스 키가 등록되지 않았습니다."
