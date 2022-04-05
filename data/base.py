import json
import xmltodict
import requests
from abc import ABCMeta, abstractmethod
from korea_public_data.core.choices import ResponseType


class PublicDataBase(metaclass=ABCMeta):
    def __init__(self):
        self.response_type = None
        self.validated_data = {}

    @property
    @abstractmethod
    def url(self):
        return None

    @abstractmethod
    def _data_valid(self):
        pass

    def _additional_processing(self, res):
        """상태에 따른 분류"""
        pass

    def _valid(self):
        """데이터 유효성 검사"""
        # 기본 유효성 검사
        assert self.url, "API URL 이 적용되지 않았습니다."
        assert self.response_type, "반환 값 종류가 적용되지 않았습니다."

        # 입력한 데이터 확인
        self._data_valid()

        # API 호출 오류 확인
        res = self._get_data()
        res.raise_for_status()

        # 데이터 입력
        self.validated_data['res'] = res

    def _get_data(self):
        """데이터 조회"""
        return requests.get(self.url)

    @staticmethod
    def json_to_dict(json_response: str):
        """JSON 딕셔너리로 전환"""
        return json.loads(json_response)

    @staticmethod
    def xml_to_dict(xml_response: str):
        """XML 딕셔너리로 전환"""
        return xmltodict.parse(xml_response)

    def _convert_response(self, res):
        """결과 타입에 따라 데이터 변환"""
        if self.response_type == ResponseType.XML:
            res = self.xml_to_dict(res.content)
        elif self.response_type == ResponseType.JSON:
            res = self.json_to_dict(res.content)
        return res

    @property
    def data(self):
        """데이터 결과 조회"""
        # 유효성 검사
        self._valid()

        # 데이터 조회
        res = self.validated_data.get('res')
        if res is None:
            raise ValueError("결과 값이 포함되어있지 않습니다.")

        # 상태에 따른 추가 처리 (오버라이딩 권장)
        self._additional_processing(res)

        # 결과 값 반환
        return self._convert_response(res)
