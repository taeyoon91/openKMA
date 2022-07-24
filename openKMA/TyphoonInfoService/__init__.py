from openKMA._common._common import *

class TyphoonInfoService: #기상청_태풍정보 조회서비스
    def __init__(self, ServiceKey:str=''):
        self.ServiceKey	= ServiceKey

    def getTyphoonInfo(self, fromTmFc:datetime, toTmFc:datetime, pageNo:int=1, numOfRows:int=999, dataType:str='XML'): #태풍정보조회
        dataType = dataType.upper()

        url = f"{domain_KMA}/{self.__class__.__name__}/{inspect.stack()[0][3]}?serviceKey={self.ServiceKey}"
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

        if isinstance(items, pd.DataFrame):
            items['service'] = inspect.stack()[0][3]

        return ResponseKMA(payload, response.url, response, resultCode, resultMsg, dataType, items)

    def getTyphoonInfoList(self, tmFc:datetime, pageNo:int=1, numOfRows:int=999, dataType:str='XML'): #태풍정보목록조회
        dataType = dataType.upper()

        url = f"{domain_KMA}/{self.__class__.__name__}/{inspect.stack()[0][3]}?serviceKey={self.ServiceKey}"
        payload = { 'pageNo'   : pageNo,
                    'numOfRows': numOfRows,
                    'dataType' : dataType,
                    'tmFc'     : tmFc.strftime('%Y%m%d')
        }

        response = request_to_kma(url, payload)
        if not isinstance(response, requests.models.Response):
            return ResponseKMA(payload, response, None, None, None, None, None)

        if dataType == 'XML':
            resultCode, resultMsg, items = transform_xml_to_dataframe(response)
        elif dataType == 'JSON':
            resultCode, resultMsg, items = transform_json_to_dataframe(response.json())

        if isinstance(items, pd.DataFrame):
            items['service'] = inspect.stack()[0][3]

        return ResponseKMA(payload, response.url, response, resultCode, resultMsg, dataType, items)

    def getTyphoonFcst(self, typSeq, tmFc:datetime, pageNo:int=1, numOfRows:int=999, dataType:str='XML'): #태풍예상정보조회
        dataType = dataType.upper()

        url = f"{domain_KMA}/{self.__class__.__name__}/{inspect.stack()[0][3]}?serviceKey={self.ServiceKey}"
        payload = { 'pageNo'   : pageNo,
                    'numOfRows': numOfRows,
                    'dataType' : dataType,
                    'typSeq'   : typSeq,
                    'tmFc': tmFc.strftime('%Y%m%d')
        }
        response = request_to_kma(url, payload)
        if not isinstance(response, requests.models.Response):
            return ResponseKMA(payload, response, None, None, None, None, None)

        if dataType == 'XML':
            resultCode, resultMsg, items = transform_xml_to_dataframe(response)
        elif dataType == 'JSON':
            resultCode, resultMsg, items = transform_json_to_dataframe(response.json())

        if isinstance(items, pd.DataFrame):
            items['service'] = inspect.stack()[0][3]

        return ResponseKMA(payload, response.url, response, resultCode, resultMsg, dataType, items)