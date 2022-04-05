from korea_public_data.data.data_go_kr.apt_trade import GetRTMSDataSvcAptTrade
from korea_public_data.data.data_go_kr.apt_trade_detail import GetRTMSDataSvcAptTradeDev
from korea_public_data.data.data_go_kr.covid_infection_status import GetCovid19InfStateJson
from korea_public_data.data.data_go_kr.nts_businessman import NTSBusinessMan
from korea_public_data.data.data_go_kr.station_by_route import GetStationByRoute
from korea_public_data.data.koreaexim_go_kr.exchange import ExchangeJSON

DATA_CLASSES = {
    "getRTMSDataSvcAptTrade": GetRTMSDataSvcAptTrade,
    "getRTMSDataSvcAptTradeDev": GetRTMSDataSvcAptTradeDev,
    "getCovid19InfStateJson": GetCovid19InfStateJson,
    "nTSBusinessMan": NTSBusinessMan,
    "getStationByRoute": GetStationByRoute,
    "exchangeJSON": ExchangeJSON
}
