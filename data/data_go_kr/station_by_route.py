from korea_public_data.core.choices import ResponseType
from korea_public_data.core.vars import default as var
from korea_public_data.core.consts import data as const
from korea_public_data.data.base import PublicDataBase


class GetStationByRoute(PublicDataBase):
    """서울특별시_노선정보조회 서비스"""
    def __init__(self, service_key: str):
        # 상위 클래스 변수 적용
        super().__init__()
        # 필수 설정
        self.service_key = service_key
        # 변수(기본 값 적용)
        self.bus_route_id = var.DEFAULT_STATION_BY_ROUTE_ID
        # 상수
        self.response_type = ResponseType.XML

    @property
    def url(self):
        return (
            f'{const.STATION_BY_ROUTE_URL}'
            f'serviceKey={self.service_key}&'
            f'busRouteId={self.bus_route_id}'
        )

    def _data_valid(self):
        """데이터 이상여부 확인"""
        assert self.service_key, "서비스 키가 등록되지 않았습니다."
