from korea_public_data.core.vars.data import DATA_CLASSES


class PublicDataController:
    def __init__(
            self,
            app: str,  # 앱 이름
    ):
        self._data_class = DATA_CLASSES.get(app)
        assert self._data_class, "선택하신 앱이 존재하지 않습니다."

    def set_keys(self, *args, **kwargs):
        """각 클래스의 키 값을 입력"""
        return self._data_class(*args, **kwargs)
