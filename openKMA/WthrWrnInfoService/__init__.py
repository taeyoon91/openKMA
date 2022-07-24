from openKMA._common._common import *

class WthrWrnInfoService: #기상청_기상특보 조회서비스
    def __init__(self, ServiceKey:str=''):
        self.ServiceKey	= ServiceKey

    def getWthrWrnList(self, stnId:int, fromTmFc:datetime, toTmFc:datetime, pageNo:int=1, numOfRows:int=999, dataType:str='XML'): #기상특보목록조회
        return self.__get_Wthr(inspect.stack()[0][3], stnId, fromTmFc, toTmFc, pageNo, numOfRows,dataType)

    def getWthrWrnMsg(self, stnId:int, fromTmFc:datetime, toTmFc:datetime, pageNo:int=1, numOfRows:int=999, dataType:str='XML'): #기상특보통보문조회
        return self.__get_Wthr(inspect.stack()[0][3], stnId, fromTmFc, toTmFc, pageNo, numOfRows,dataType)

    def getWthrInfoList(self, stnId:int, fromTmFc:datetime, toTmFc:datetime, pageNo:int=1, numOfRows:int=999, dataType:str='XML'): #기상정보목록조회
        return self.__get_Wthr(inspect.stack()[0][3], stnId, fromTmFc, toTmFc, pageNo, numOfRows,dataType)

    def getWthrInfo(self, stnId:int, fromTmFc:datetime, toTmFc:datetime, pageNo:int=1, numOfRows:int=999, dataType:str='XML'): #기상정보문조회
        return self.__get_Wthr(inspect.stack()[0][3], stnId, fromTmFc, toTmFc, pageNo, numOfRows,dataType)

    def getWthrBrkNewsList(self, stnId:int, fromTmFc:datetime, toTmFc:datetime, pageNo:int=1, numOfRows:int=999, dataType:str='XML'): #기상속보목록조회
        return self.__get_Wthr(inspect.stack()[0][3], stnId, fromTmFc, toTmFc, pageNo, numOfRows,dataType)

    def getWthrBrkNews(self, stnId:int, fromTmFc:datetime, toTmFc:datetime, pageNo:int=1, numOfRows:int=999, dataType:str='XML'): #기상속보조회
        return self.__get_Wthr(inspect.stack()[0][3], stnId, fromTmFc, toTmFc, pageNo, numOfRows,dataType)

    def getWthrPwnList(self, stnId:int, fromTmFc:datetime, toTmFc:datetime, pageNo:int=1, numOfRows:int=999, dataType:str='XML'): #기상예비특보목록조회
        return self.__get_Wthr(inspect.stack()[0][3], stnId, fromTmFc, toTmFc, pageNo, numOfRows,dataType)

    def getWthrPwn(self, stnId:int, fromTmFc:datetime, toTmFc:datetime, pageNo:int=1, numOfRows:int=999, dataType:str='XML'): #기상예비특보조회
        return self.__get_Wthr(inspect.stack()[0][3], stnId, fromTmFc, toTmFc, pageNo, numOfRows,dataType)

    def getPwnCd(self, stnId:int, warningType:int, areaCode:str, fromTmFc:datetime, toTmFc:datetime, pageNo:int=1, numOfRows:int=999, dataType:str='XML'): #특보코드조회
        dataType = dataType.upper()

        url = f"{domain_KMA}/{self.__class__.__name__}/{inspect.stack()[0][3]}?serviceKey={self.ServiceKey}"
        payload = { 'pageNo'   : pageNo,
                    'numOfRows': numOfRows,
                    'dataType' : dataType,
                    'stnId'    : stnId,
                    'warningType': warningType,
                    'areaCode'   : areaCode,
                    'fromTmFc': fromTmFc.strftime('%Y%m%d'),
                    'toTmFc'  : toTmFc.strftime('%Y%m%d')
        }

        response = request_to_kma(url, payload)
        if not isinstance(response, requests.models.Response):
            return ResponseKMA(payload, response, None, None, None, None, None)
        
        if dataType == 'XML':
            resultCode, resultMsg, items = transform_xml_to_dataframe(response)
        elif dataType == 'JSON':
            resultCode, resultMsg, items = transform_json_to_dataframe(response.json())

        if isinstance(items, pd.DataFrame):
            items['service'] = 'getPwnCd'

        return ResponseKMA(payload, response.url, response, resultCode, resultMsg, dataType, items)


    def getPwnStatus(self, pageNo:int=1, numOfRows:int=999, dataType:str='XML'): #특보현황조회
        dataType = dataType.upper()

        url = f"{domain_KMA}/{self.__class__.__name__}/{inspect.stack()[0][3]}?serviceKey={self.ServiceKey}"
        payload = { 'pageNo'   : pageNo,
                    'numOfRows': numOfRows,
                    'dataType' : dataType
        }

        response = request_to_kma(url, payload)
        if not isinstance(response, requests.models.Response):
            return ResponseKMA(payload, response, None, None, None, None, None)
        
        if dataType == 'XML':
            resultCode, resultMsg, items = transform_xml_to_dataframe(response)
        elif dataType == 'JSON':
            resultCode, resultMsg, items = transform_json_to_dataframe(response.json())

        if isinstance(items, pd.DataFrame):
            items['service'] = 'getPwnStatus'

        return ResponseKMA(payload, response.url, response, resultCode, resultMsg, dataType, items)

    def __get_Wthr(self, service, stnId, fromTmFc, toTmFc, pageNo, numOfRows, dataType):
        dataType = dataType.upper()

        url = f"{domain_KMA}/{self.__class__.__name__}/{service}?serviceKey={self.ServiceKey}"
        payload = { 'pageNo'   : pageNo,
                    'numOfRows': numOfRows,
                    'dataType' : dataType,
                    'stnId'   : stnId,
                    'fromTmFc': fromTmFc.strftime('%Y%m%d'),
                    'toTmFc'  : toTmFc.strftime('%Y%m%d')
        }

        response = request_to_kma(url, payload)
        if not isinstance(response, requests.models.Response):
            return ResponseKMA(payload, response, None, None, None, None, None)

        if dataType == 'XML':
            resultCode, resultMsg, items = transform_xml_to_dataframe(response)
        elif dataType == 'JSON':
            resultCode, resultMsg, items = transform_json_to_dataframe(response.json())

        if isinstance(items, pd.DataFrame):
            items['service'] = service

        return ResponseKMA(payload, response.url, response, resultCode, resultMsg, dataType, items)