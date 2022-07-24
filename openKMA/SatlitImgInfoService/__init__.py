from numpy import sort
from openKMA._common._common import *

class SatlitImgInfoService: #기상청_위성영상 조회서비스
    def __init__(self, ServiceKey:str=''):
        self.ServiceKey	= ServiceKey

    def getInsightSatlit(self, sat:str, data:str, area:str, time:datetime, pageNo=1, numOfRows=999, dataType='XML'): #천리안위성조회
        dataType = dataType.upper()

        url = f"{domain_KMA}/{self.__class__.__name__}/{inspect.stack()[0][3]}?serviceKey={self.ServiceKey}"
        payload = { 'pageNo'   : pageNo,
                    'numOfRows': numOfRows,
                    'dataType' : dataType,
                    'sat'  : sat,
                    'data' : data,
                    'area' : area,
                    'time' : time.strftime('%Y%m%d')
        }
        response = request_to_kma(url, payload)
        if not isinstance(response, requests.models.Response):
            return ResponseKMA(payload, response, None, None, None, None, None)

        if dataType == 'XML':
            resultCode, resultMsg, items = transform_xml_to_dataframe(response)
        elif dataType == 'JSON':
            resultCode, resultMsg, items = transform_json_to_dataframe(response.json())

        files = []
        for _, item in items.iterrows():
            files.extend(item['satImgC-file'])
        files = sorted(files)
        items = pd.DataFrame({'satImgC-file':files})

        return ResponseKMA(payload, response.url, response, resultCode, resultMsg, dataType, items)