from korea_public_data.data.base import PublicDataBase
from korea_public_data.data import *


class PublicDataController:
    def __init__(
            self,
            app: str,  # 앱 이름
    ):
        assert app and type(app) == str and len(app) > 0, "앱 이름이 없습니다."
        # 앱 이름 설정
        app_name = str(app[0]).upper() + app[1:]
        # 데이터 클래스 조회
        data_classes = {cls.__name__: cls for cls in PublicDataBase.__subclasses__()}
        self._data_class = data_classes.get(app_name)
        assert self._data_class, "선택하신 앱이 존재하지 않습니다."

    def set_keys(self, *args, **kwargs):
        """각 클래스의 키 값을 입력"""
        return self._data_class(*args, **kwargs)
