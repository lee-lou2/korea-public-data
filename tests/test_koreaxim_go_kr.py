from os import environ

from korea_public_data.service.app import PublicDataController


def test_exchange():
    """환율 조회 API"""
    # 앱 실행
    auth_key = environ.get("KOREA_BANK_AUTH_KEY")
    app_name = 'exchangeJSON'

    if auth_key:
        controller = PublicDataController(app_name).set_keys(
            auth_key=auth_key
        )
        assert type(controller.data) == list
