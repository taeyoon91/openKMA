from openKMA._common._common import *

class EqkInfoService: #기상청_지진정보 조회서비스
    def __init__(self, ServiceKey:str=''):
        self.ServiceKey	= ServiceKey

    def getEqkMsg(self, fromTmFc:datetime, toTmFc:datetime, pageNo:int=1, numOfRows:int=999, dataType:str='XML'):#지진통보문조회
        return self.__get(inspect.stack()[0][3], fromTmFc, toTmFc, pageNo, numOfRows, dataType)
    
    def getEqkMsgList(self, fromTmFc:datetime, toTmFc:datetime, pageNo:int=1, numOfRows:int=999, dataType:str='XML'):#지진통보문 목록조회
        return self.__get(inspect.stack()[0][3], fromTmFc, toTmFc, pageNo, numOfRows, dataType)

    def getTsunamiMsg(self, fromTmFc:datetime, toTmFc:datetime, pageNo:int=1, numOfRows:int=999, dataType:str='XML'): #지진해일통보문조회
        return self.__get(inspect.stack()[0][3], fromTmFc, toTmFc, pageNo, numOfRows, dataType)

    def getTsunamiMsgList(self, fromTmFc:datetime, toTmFc:datetime, pageNo:int=1, numOfRows:int=999, dataType:str='XML'): #지진해일통보문 목록조회
        return self.__get(inspect.stack()[0][3], fromTmFc, toTmFc, pageNo, numOfRows, dataType)
    
    def __get(self, service, fromTmFc, toTmFc, pageNo, numOfRows, dataType):
        dataType = dataType.upper()

        url = f"{domain_KMA}/{self.__class__.__name__}/{service}?serviceKey={self.ServiceKey}"
        payload = { 'pageNo'   : pageNo,
                    'numOfRows': numOfRows,
                    'dataType' : dataType,
                    'fromTmFc' : fromTmFc.strftime('%Y%m%d'),
                    'toTmFc'   :   toTmFc.strftime('%Y%m%d')
        }

        response = request_to_kma(url, payload)
        if not isinstance(response, requests.models.Response):
            return ResponseKMA(payload, response, None, None, None, None, None)

        if dataType == 'XML':
            resultCode, resultMsg, items = transform_xml_to_dataframe(response)
        elif dataType == 'JSON':
            resultCode, resultMsg, items = transform_json_to_dataframe(response.json())

        return ResponseKMA(payload, response.url, response, resultCode, resultMsg, dataType, items)