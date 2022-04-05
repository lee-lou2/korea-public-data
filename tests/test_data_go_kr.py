from collections import OrderedDict
from os import environ

from korea_public_data.service.app import PublicDataController


def create_app_and_status_check(app_name, service_key, **kwargs):
    controller = PublicDataController(app_name).set_keys(
        service_key=service_key, **kwargs
    )

    # 데이터 검증
    if service_key:
        res = controller.data
        assert isinstance(controller.data, OrderedDict)
        assert res.get('response').get('header').get('resultCode') in ['00', '99']
        assert res.get('response').get('header').get('resultMsg') in [
            'NORMAL SERVICE.', 'SERVICE KEY IS NOT REGISTERED ERROR.'
        ]

        return res
    else:
        try:
            controller.data
        except Exception as ex:
            assert str(ex) == "서비스 키가 등록되지 않았습니다."


def test_request_apt_trade_api():
    """아파트 매매 API"""
    # 앱 실행
    service_key = environ.get("DATA_GO_KR_SERVICE_KEY")
    app_name = 'getRTMSDataSvcAptTrade'
    res = create_app_and_status_check(app_name, service_key)


def test_request_apt_trade_dev_api():
    """아파트 매매 상세 API"""
    # 앱 실행
    service_key = environ.get("DATA_GO_KR_SERVICE_KEY")
    app_name = 'getRTMSDataSvcAptTradeDev'
    res = create_app_and_status_check(app_name, service_key)


def test_request_covid():
    """코로나 감염 현황 API"""
    # 앱 실행
    service_key = environ.get("DATA_GO_KR_SERVICE_KEY")
    app_name = 'getCovid19InfStateJson'
    res = create_app_and_status_check(app_name, service_key)


def test_request_business_man():
    """사업자 등록정보 진위확인 및 상태조회 서비스 API"""
    # 앱 실행
    service_key = environ.get("DATA_GO_KR_SERVICE_KEY")
    app_name = 'nTSBusinessMan'

    if service_key:
        # 기본 사업자 조회
        controller = PublicDataController(app_name).set_keys(
            service_key=service_key
        )
        res = controller.data
        assert res.get("request_cnt") == 1
        assert res.get("data")[0].get("b_no") == "1208147521"

        # 변경된 사업자 조회
        controller.business_no = ["2208162517"]
        res = controller.data
        assert res.get("request_cnt") == 1
        assert res.get("data")[0].get("b_no") == "2208162517"


def test_station_by_route():
    """서울 버스 노선 정보 API"""
    # 앱 실행
    service_key = environ.get("DATA_GO_KR_SERVICE_KEY")
    app_name = 'getStationByRoute'

    if service_key:
        controller = PublicDataController(app_name).set_keys(
            service_key=service_key
        )
        assert isinstance(controller.data, OrderedDict)


def test_so_city_stats():
    """지역별 성범죄자 통계 API"""
    # 앱 실행
    app_name = 'sOCityStats'
    controller = PublicDataController(app_name).set_keys()
    res = controller.data

    assert isinstance(res, OrderedDict)
    assert res.get("Result").get("Code") == "00"


