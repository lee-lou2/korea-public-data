from datetime import datetime, timedelta

import pytz as pytz


DEFAULT_APT_TRADE_LOCATION_CODE = "00440"
DEFAULT_YESTERDAY_SEOUL_TIMEZONE = datetime.now().astimezone(pytz.timezone("Asia/Seoul")) - timedelta(days=1)
DEFAULT_TODAY_SEOUL_TIMEZONE = datetime.now().astimezone(pytz.timezone("Asia/Seoul"))
DEFAULT_PAGE_NO = 1
DEFAULT_PAGE_NUM_OF_ROWS = 100
DEFAULT_STATION_BY_ROUTE_ID = "14194"
DEFAULT_BUSINESS_MAN_NUMBER = ["1208147521"]
DEFAULT_ITEM_PER_PAGE = 10
DEFAULT_MULTI_MOVIE_YN = None
DEFAULT_REP_NATION_CD = None
DEFAULT_WIDE_AREA_CD = None

