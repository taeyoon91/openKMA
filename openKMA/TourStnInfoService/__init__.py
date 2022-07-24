from openKMA._common._common import *

class TourStnInfoService: #기상청_관광코스별 관광지 상세 날씨 조회서비스
    def __init__(self, ServiceKey:str=''):
        self.ServiceKey	= ServiceKey

    def getTourStnVilageFcst(self, COURSE_ID:int, CURRENT_DATE:datetime, HOUR:int, pageNo:int=1, numOfRows:int=999, dataType:str='XML'): #동네예보조회
        return self.__getTourStn(inspect.stack()[0][3], COURSE_ID, CURRENT_DATE, HOUR, pageNo, numOfRows, dataType)

    def getTourStnWthrIdx(self, COURSE_ID:int, CURRENT_DATE:datetime, HOUR:int, pageNo:int=1, numOfRows:int=999, dataType:str='XML'): #기상지수예보조회
        return self.__getTourStn(inspect.stack()[0][3], COURSE_ID, CURRENT_DATE, HOUR, pageNo, numOfRows, dataType)

    def getCityTourClmIdx(self, CITY_AREA_ID:str, CURRENT_DATE:datetime, DAY:int, pageNo=1, numOfRows=999, dataType='XML'): #시군구별관광기후지수조회
        dataType = dataType.upper()

        url = f"{domain_KMA}/{self.__class__.__name__}/{inspect.stack()[0][3]}?serviceKey={self.ServiceKey}"
        payload = { 'pageNo'   : pageNo,
                    'numOfRows': numOfRows,
                    'dataType' : dataType,
                    'CITY_AREA_ID'   : CITY_AREA_ID,
                    'CURRENT_DATE': CURRENT_DATE.strftime('%Y%m%d'),
                    'DAY'  : DAY
        }

        response = request_to_kma(url, payload)
        if not isinstance(response, requests.models.Response):
            return ResponseKMA(payload, response, None, None, None, None, None)

        if dataType == 'XML':
            resultCode, resultMsg, items = transform_xml_to_dataframe(response)
        elif dataType == 'JSON':
            resultCode, resultMsg, items = transform_json_to_dataframe(response.json())

        return ResponseKMA(payload, response.url, response, resultCode, resultMsg, dataType, items)

    def __getTourStn(self, service, COURSE_ID, CURRENT_DATE, HOUR, pageNo, numOfRows, dataType):
        dataType = dataType.upper()

        url = f"{domain_KMA}/{self.__class__.__name__}/{service}?serviceKey={self.ServiceKey}"
        payload = { 'pageNo'   : pageNo,
                    'numOfRows': numOfRows,
                    'dataType' : dataType,
                    'COURSE_ID'   : COURSE_ID,
                    'CURRENT_DATE': CURRENT_DATE.strftime('%Y%m%d'),
                    'HOUR'  : HOUR
        }
        response = request_to_kma(url, payload)
        if not isinstance(response, requests.models.Response):
            return ResponseKMA(payload, response, None, None, None, None, None)

        if dataType == 'XML':
            resultCode, resultMsg, items = transform_xml_to_dataframe(response)
        elif dataType == 'JSON':
            resultCode, resultMsg, items = transform_json_to_dataframe(response.json())

        return ResponseKMA(payload, response.url, response, resultCode, resultMsg, dataType, items)