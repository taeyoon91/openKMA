from openKMA._common._common import *

class VilageFcstMsgService: #기상청_동네예보 통보문 조회서비스
    def __init__(self, ServiceKey:str=''):
        self.ServiceKey	= ServiceKey

    def getWthrSituation(self, stnId:int, pageNo:int=1, numOfRows:int=999, dataType:str='XML'): #기상개황조회
        dataType = dataType.upper()

        url = f"{domain_KMA}/{self.__class__.__name__}/{inspect.stack()[0][3]}?serviceKey={self.ServiceKey}"
        payload = { 'pageNo'   : pageNo,
                    'numOfRows': numOfRows,
                    'dataType' : dataType,
                    'stnId': stnId
        }

        response = request_to_kma(url, payload)
        if not isinstance(response, requests.models.Response):
            return ResponseKMA(payload, response, None, None, None, None, None)

        if dataType == 'XML':
            resultCode, resultMsg, items = transform_xml_to_dataframe(response)
        elif dataType == 'JSON':
            resultCode, resultMsg, items = transform_json_to_dataframe(response.json())

        if isinstance(items, pd.DataFrame):
            items.set_index('tmFc',inplace=True);items.index = pd.to_datetime(items.index)
            items['requestTime']  = pd.to_datetime(datetime.now())
            items['service'] = 'getWthrSituation'

        return ResponseKMA(payload, response.url, response, resultCode, resultMsg, dataType, items)

    def getLandFcst(self, regId:str, pageNo:int=1, numOfRows:int=999, dataType:str='XML'): #육상예보조회
        return self.__get_Fcst(inspect.stack()[0][3], regId, pageNo, numOfRows, dataType)

    def getSeaFcst(self, regId:str, pageNo:int=1, numOfRows:int=999, dataType:str='XML'): #해상예보조회
        return self.__get_Fcst(inspect.stack()[0][3], regId, pageNo, numOfRows, dataType)

    def __get_Fcst(self, service, regId, pageNo, numOfRows, dataType):
        dataType = dataType.upper()

        url = f"{domain_KMA}/{self.__class__.__name__}/{service}?serviceKey={self.ServiceKey}"
        payload = { 'pageNo'   : pageNo,
                    'numOfRows': numOfRows,
                    'dataType' : dataType,
                    'regId': regId
        }
        response = request_to_kma(url, payload)
        if not isinstance(response, requests.models.Response):
            return ResponseKMA(payload, response, None, None, None, None, None)

        if dataType == 'XML':
            resultCode, resultMsg, items = transform_xml_to_dataframe(response)
        elif dataType == 'JSON':
            resultCode, resultMsg, items = transform_json_to_dataframe(response.json())

        if isinstance(items, pd.DataFrame):
            if   service == 'getLandFcst':
                items['announceTime'] = pd.to_datetime(items['announceTime'], format='%Y%m%d%H%M')
            elif service == 'getSeaFcst':
                items['tmFc'] = pd.to_datetime(items['tmFc'], format='%Y%m%d%H%M')
            items = items.set_index('numEf')
            items['service'] = service

        return ResponseKMA(payload, response.url, response, resultCode, resultMsg, dataType, items)