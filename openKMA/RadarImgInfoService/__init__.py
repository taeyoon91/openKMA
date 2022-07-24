from openKMA._common._common import *

class RadarImgInfoService: #기상청_레이더영상 조회서비스
    def __init__(self, ServiceKey:str=''):
        self.ServiceKey	= ServiceKey

    def getCmpImg(self, time:datetime, data:str='CMP_WRC', pageNo:int=1, numOfRows:int=999, dataType:str='XML'): #레이더합성영상조회
        dataType = dataType.upper()

        url = f"{domain_KMA}/{self.__class__.__name__}/{inspect.stack()[0][3]}?serviceKey={self.ServiceKey}"
        payload = { 'pageNo'   : pageNo,
                    'numOfRows': numOfRows,
                    'dataType' : dataType,
                    'data' : data,
                    'time' : time.strftime('%Y%m%d')
        }
        response = request_to_kma(url, payload)
        if not isinstance(response, requests.models.Response):
            return ResponseKMA(payload, response, None, None, None, None, None)

        if dataType == 'XML':
            resultCode, resultMsg, items = transform_xml_to_dataframe(response)
        elif dataType == 'JSON':
            resultCode, resultMsg, items = transform_json_to_dataframe(response.json())

        files = pd.DataFrame()
        for _, item in items.iterrows():
            files = pd.concat([files, pd.DataFrame(item['rdr-img-file'], columns=['rdr-img-file'])])
        files.reset_index(drop=True, inplace=True)

        return ResponseKMA(payload, response.url, response, resultCode, resultMsg, dataType, files)

    def getRadarIndvdlzImg(self, doc:str, time:datetime, pageNo:int=1, numOfRows:int=999, dataType:str='XML'): #레이더개별영상조회
        dataType = dataType.upper()

        url = f"{domain_KMA}/{self.__class__.__name__}/{inspect.stack()[0][3]}?serviceKey={self.ServiceKey}"
        payload = { 'pageNo'   : pageNo,
                    'numOfRows': numOfRows,
                    'dataType' : dataType,
                    'doc'  : doc,
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
            files.extend(item['rdr-dnh'])
        files = sorted(files)
        items = pd.DataFrame({'rdr-dnh':files})

        return ResponseKMA(payload, response.url, response, resultCode, resultMsg, dataType, items)