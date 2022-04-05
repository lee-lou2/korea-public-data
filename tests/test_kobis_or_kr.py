from os import environ

from korea_public_data.service.app import PublicDataController


def test_request_apt_trade_api():
    """일별 박스 오피스 순위 API"""
    # 앱 실행
    key = environ.get("KOBIS_OR_KR_KEY")
    app_name = 'searchDailyBoxOfficeList'

    if key:
        # 기본 사업자 조회
        controller = PublicDataController(app_name).set_keys(
            key=key
        )
        res = controller.data
        assert res.get("boxOfficeResult").get("boxofficeType") == "일별 박스오피스"
