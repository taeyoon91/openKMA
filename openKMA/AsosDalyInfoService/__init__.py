from openKMA._common._common import *

class AsosDalyInfoService: #기상청_지상(종관, ASOS) 일자료 조회서비스
    def __init__(self, ServiceKey=''):
        self.ServiceKey	= ServiceKey

    def getWthrDataList(self, stnIds:int, startDt:datetime, endDt:datetime, pageNo:int=1, numOfRows:int=999, dataType:str='XML'):
        dataType = dataType.upper()
        
        startDt = startDt.replace(hour= 0, minute=0, second=0, microsecond=0)
        endDt   =   endDt.replace(hour=23, minute=0, second=0, microsecond=0)

        url = f"{domain_KMA}/{self.__class__.__name__}/{inspect.stack()[0][3]}?serviceKey={self.ServiceKey}"
        payload = { 'pageNo': pageNo,
                    'numOfRows':numOfRows,
                    'dataType':dataType,
                    'dataCd':'ASOS',
                    'dateCd':'DAY',
                    'startDt':startDt.strftime('%Y%m%d'),
                    'endDt':endDt.strftime('%Y%m%d'),
                    'stnIds':stnIds
        }

        response = request_to_kma(url, payload)
        if not isinstance(response, requests.models.Response):
            return ResponseKMA(payload, response, None, None, None, None, None)

        if   dataType == 'XML' :
            resultCode, resultMsg, items = transform_xml_to_dataframe(response)
        elif dataType == 'JSON':
            resultCode, resultMsg, items = transform_json_to_dataframe(response.json())

        if isinstance(items, pd.DataFrame):
            timestamp = pd.DataFrame(index=(pd.date_range(startDt, endDt, freq='D')))
            items.set_index('tm',inplace=True)
            items.index = pd.to_datetime(items.index)
            items = pd.concat([ timestamp, items ],axis=1)

        return ResponseKMA(payload, response.url, response, resultCode, resultMsg, dataType, items)
