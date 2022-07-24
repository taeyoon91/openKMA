# AsosHourlyInfoService: #기상청_지상(종관, ASOS) 시간자료 조회서비스
from openKMA._common._common import *


class AsosHourlyInfoService: #기상청_지상(종관, ASOS) 시간자료 조회서비스
    def __init__(self, ServiceKey=''):
        self.ServiceKey	= ServiceKey

    def getWthrDataList(self, stnIds, startDtHh:datetime, endDtHh:datetime, pageNo:int=1, numOfRows:int=999, dataType:str='XML'):
        
        dataType = dataType.upper()

        startDtHh = startDtHh.replace(minute=0, second=0, microsecond=0)
        endDtHh   =   endDtHh.replace(minute=0, second=0, microsecond=0)

        url = f"{domain_KMA}/{self.__class__.__name__}/getWthrDataList?serviceKey={self.ServiceKey}"
        payload = { 'pageNo'   : pageNo,
                    'numOfRows': numOfRows,
                    'dataType' : dataType,
                    'dataCd':'ASOS',
                    'dateCd':'HR',
                    'startDt': startDtHh.strftime('%Y%m%d'),
                    'startHh': startDtHh.strftime('%H'),
                    'endDt'  : endDtHh.strftime('%Y%m%d'),
                    'endHh'  : endDtHh.strftime('%H'),
                    'stnIds' : stnIds
        }

        response = requests_to_kma(url, payload)
        if not isinstance(response, requests.models.Response):
            return ResponseKMA(payload, response, None, None, None, None, None)

        if dataType == 'XML':
            resultCode, resultMsg, items = transform_xml_to_dataframe(response)
        elif dataType == 'JSON':
            resultCode, resultMsg, items = transform_json_to_dataframe(response.json())

        timestamp = pd.DataFrame(index=(pd.date_range(startDtHh, endDtHh, freq='H')))
        items.set_index('tm',inplace=True)
        items.index = pd.to_datetime(items.index)
        items = pd.concat([ timestamp, items ],axis=1)

        return ResponseKMA(payload, response.url, response, resultCode, resultMsg, dataType, items)
