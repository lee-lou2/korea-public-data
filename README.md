# Korea Public DATA
> 공공 데이터를 간편히 조회 할 수 있는 파이썬 라이브러리


## Website
- Pypi : https://pypi.org/project/korea-public-data/


## Install

```sh
pip install korea-public-data
```


## Example
```sh
# ------------------------
# 국토교통부_아파트매매 실거래자료
# ------------------------
service_key = <서비스 키>
app_name = "getRTMSDataSvcAptTrade"  # 앱

controller = PublicDataController(app_name).set_keys(
  service_key=service_key
)
# 기본 데이터 조회
controller.data  # 마포, 어제 일자로 데이터 조회

# 변수 변경
controller.location_code = <지역 코드>
controller.date_to_str = <조회 일(YYYYMM)>
controller.data  # 원하는 지역, 일자 데이터 조회
```


## Apps
| 구분                            | 앱                    | 파라미터 정보                                                                                                                      |
|-------------------------------|----------------------|------------------------------------------------------------------------------------------------------------------------------|
| 국토교통부_아파트매매 실거래자료             | getRTMSDataSvcAptTrade | **service_key(str)**, location_code(str), search_date(str: YYYYMM)                                                           |
| 국토교통부_아파트매매 실거래 상세 자료         |getRTMSDataSvcAptTradeDev| **service_key(str)**, location_code(str), search_date(str: YYYYMM), page_no(int), num_of_rows(int)                           |
| 공공데이터활용지원센터_보건복지부 코로나19 감염 현황 |getCovid19InfStateJson| **service_key(str)**, start_at(str: YYYYMMDD), end_at(str: YYYYMMDD), page_no(int), num_of_rows(int)                         |
| 사업자 등록정보 진위확인 및 상태조회          |nTSBusinessMan| **service_key(str)**, business_no(list)                                                                                      |
| 서울 버스 노선 정보                   |getStationByRoute| **service_key(str)**, bus_route_id(str)                                                                                      |
| 현재 환율 API                     |exchangeJSON| **auth_key(str)**, search_date(str: YYYYMMDD)                                                                                |                                                     |
| 지역별 성범죄자 통계|sOCityStats| -                                                                                                                            |                                                     |
| 일별 박스 오피스 순위|searchDailyBoxOfficeList| **key(str)**, target_dt(str: YYYYMMDD), item_per_page(str), multi_movie_yn(Y or N), rep_nation_cd(K or F), wide_area_cd(str) |

*변수 중 **굵게** 표시된 부분은 Controller 생성시 사용되는 파라미터입니다*


## Environment

프로그램 실행을 위해선 아래 버전 준수가 요구됩니다.

```sh
Python 3.7 이상
```


## Release Note

* 0.0.1
  * 최초 배포
  * 범용적 데이터 조회 구조 제작
  * 사용자의 편의를 최우선으로 고려
  * 기본 데이터가 입력되어있어 간단히 테스트 가능

* 0.0.2-3
  * 참조 라이브러리 추가
  * README 수정(홈페이지 적용 등)

* 0.0.4
  * 기능 추가(지역별 성범죄자 통계 및 일별 박스 오피스 등)
  * 불필요한 코드 제거
  * 클래스 참조 방식 변경

## Thank You

우선 해당 라이브러리에 관심을 주셔서 감사합니다.

많은 서비스를 간편히 사용할 수 있도록 지속적으로 업데이트 할 예정입니다.

추가 문의나 요청 사항 등이 있으시면 아래 이메일로 문의주세요.


## Contact

JAY | root@ja-y.com
