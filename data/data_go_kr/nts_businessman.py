import json
import requests

from korea_public_data.core.choices import ResponseType
from korea_public_data.core.vars import default as var
from korea_public_data.core.consts import data as const
from korea_public_data.data.base import PublicDataBase


class NTSBusinessMan(PublicDataBase):
    """국세청_사업자등록정보 진위확인 및 상태조회 서비스"""
    def __init__(self, service_key: str):
        # 상위 클래스 변수 적용
        super().__init__()
        # 필수 설정
        self.service_key = service_key
        self.business_no = var.DEFAULT_BUSINESS_MAN_NUMBER
        # 상수
        self.response_type = ResponseType.JSON

    @property
    def url(self):
        return (
            f'{const.NTS_BUSINESS_MAN_URL}'
            f'serviceKey={self.service_key}'
        )

    def _get_data(self):
        """데이터 조회"""
        headers = {"Content-Type": "application/json"}
        data = {"b_no": self.business_no}
        return requests.post(self.url, data=json.dumps(data), headers=headers)

    def _data_valid(self):
        """데이터 이상여부 확인"""
        assert self.service_key, "서비스 키가 등록되지 않았습니다."
        assert self.business_no, "조회할 사업자 번호가 필요합니다."
        assert type(self.business_no) == list, "리스트의 형태만 검색이 가능합니다."