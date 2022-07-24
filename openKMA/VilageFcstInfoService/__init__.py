from openKMA._common._common import *

class VilageFcstInfoService: #기상청_단기예보 ((구)_동네예보) 조회서비스
    def __init__(self, ServiceKey:str=''):
        self.ServiceKey	= ServiceKey

    def getVilageFcst(self, X:int, Y:int, basetime:datetime, pageNo:int=1, numOfRows:int=999, dataType:str='XML'):
        basetime = self.__get_baseTime_VilageFcst(basetime)
        return self.__get_Fcst(inspect.stack()[0][3], X, Y, basetime, pageNo, numOfRows, dataType)

    def getUltraSrtFcst(self, X:int, Y:int, basetime:datetime, pageNo:int=1, numOfRows:int=999, dataType:str='XML'):
        basetime = self.__get_baseTime_UltraSrtFcst(basetime)
        return self.__get_Fcst(inspect.stack()[0][3], X, Y, basetime, pageNo, numOfRows, dataType)

    def getUltraSrtNcst(self, X:int, Y:int, basetime:datetime, pageNo:int=1, numOfRows:int=999, dataType:str='XML'):
        basetime = self.__get_baseTime_UltraSrtNcst(basetime)
        return self.__get_Ncst(inspect.stack()[0][3], X, Y, basetime, pageNo, numOfRows, dataType)

    def getFcstVersion(self, ftype:str, basedatetime:datetime, pageNo:int=1, numOfRows:int=999, dataType:str='XML'):
        assert ftype in ['ODAM','VSRT','SHRT'], \
            f"ftype shoud be one of 'ODAM'/'VSRT'/'SHRT', (UltraSrtNcst-ODAM, UltraSrtFcst-VSRT, VilageFcst-SHRT)"
        if   ftype == 'ODAM': basedatetime = self.__get_baseTime_UltraSrtNcst(basedatetime)
        elif ftype == 'VSRT': basedatetime = self.__get_baseTime_UltraSrtFcst(basedatetime)
        elif ftype == 'SHRT': basedatetime = self.__get_baseTime_VilageFcst(  basedatetime)

        dataType = dataType.upper()

        url = f"{domain_KMA}/VilageFcstInfoService_2.0/{inspect.stack()[0][3]}?serviceKey={self.ServiceKey}"
        payload = { 'pageNo'   : pageNo,
                    'numOfRows': numOfRows,
                    'dataType' : dataType,
                    'ftype'    : ftype,
                    'basedatetime': basedatetime.strftime('%Y%m%d%H%M')
        }

        response = request_to_kma(url, payload)
        if not isinstance(response, requests.models.Response):
            return ResponseKMA(payload, response, None, None, None, None, None)

        if dataType == 'XML':
            resultCode, resultMsg, items = transform_xml_to_dataframe(response)
        elif dataType == 'JSON':
            resultCode, resultMsg, items = transform_json_to_dataframe(response.json())

        if isinstance(items, pd.DataFrame):
            items['basedatetime'] = pd.to_datetime(basedatetime)
            items['version'] = pd.to_datetime(items['version'], format='%Y%m%d%H%M%S')
            items['service'] = 'getFcstVersion'

        return ResponseKMA(payload, response.url, response, resultCode, resultMsg, dataType, items)
    
    def __get_Fcst(self, service, X, Y, basetime, pageNo, numOfRows, dataType):
        dataType = dataType.upper()

        url = f"{domain_KMA}/VilageFcstInfoService_2.0/{service}?serviceKey={self.ServiceKey}"
        payload = { 'pageNo'   : pageNo,
                    'numOfRows': numOfRows,
                    'dataType' : dataType,
                    'base_date': basetime.strftime('%Y%m%d'),
                    'base_time': basetime.strftime('%H%M'),
                    'nx': X,
                    'ny': Y
        }

        response = request_to_kma(url, payload)
        if not isinstance(response, requests.models.Response):
            return ResponseKMA(payload, response, None, None, None, None, None)

        if dataType == 'XML':
            resultCode, resultMsg, items = transform_xml_to_dataframe(response)
        elif dataType == 'JSON':
            resultCode, resultMsg, items = transform_json_to_dataframe(response.json())

        if isinstance(items, pd.DataFrame):
            items['fcstDateTime'] = items['fcstDate'] + items['fcstTime']
            baseDateTime = items['baseDate'][0] + items['baseTime'][0]
            nx = items['nx'][0];ny = items['ny'][0]
            items.set_index(pd.to_datetime(items['fcstDateTime'],format="%Y%m%d%H%M"),inplace=True)
            items = items.groupby([items.index, 'category'])['fcstValue'].aggregate('first').unstack()
            items = items.to_dict('index');items = pd.DataFrame.from_dict(items, orient='index')
            items['nx']=nx;items['ny']=ny
            items['baseDateTime'] = pd.to_datetime(baseDateTime,format="%Y%m%d%H%M")
            items['service']=service
            items.index.name = 'fcstDateTime'

        return ResponseKMA(payload, response.url, response, resultCode, resultMsg, dataType, items)

    def __get_Ncst(self, service, X, Y, basetime, pageNo, numOfRows, dataType):
        dataType = dataType.upper()

        url = f"{domain_KMA}/VilageFcstInfoService_2.0/{service}?serviceKey={self.ServiceKey}"
        payload = { 'pageNo'   : pageNo,
                    'numOfRows': numOfRows,
                    'dataType' : dataType,
                    'base_date': basetime.strftime('%Y%m%d'),
                    'base_time': basetime.strftime('%H%M'),
                    'nx': X,
                    'ny': Y
        }

        response = request_to_kma(url, payload)
        if not isinstance(response, requests.models.Response):
            return ResponseKMA(payload, response, None, None, None, None, None)

        if dataType == 'XML':
            resultCode, resultMsg, items = transform_xml_to_dataframe(response)
        elif dataType == 'JSON':
            resultCode, resultMsg, items = transform_json_to_dataframe(response.json())

        if isinstance(items, pd.DataFrame):
            items['baseDateTime'] = items['baseDate'] + items['baseTime']
            nx = items['nx'][0];ny = items['ny'][0]
            items.set_index(pd.to_datetime(items['baseDateTime'],format="%Y%m%d%H%M"),inplace=True)
            items = items.groupby([items.index, 'category'])['obsrValue'].aggregate('first').unstack()
            items = items.to_dict('index');items = pd.DataFrame.from_dict(items, orient='index')
            items['nx']=nx;items['ny']=ny;items['service']='UltraSrtNcst'
            items.index.name = 'baseDateTime'

        return ResponseKMA(payload, response.url, response, resultCode, resultMsg, dataType, items)

    def __get_baseTime_VilageFcst(self, time):
        h = time.hour
        if h < 2:
            time = time + timedelta(days=-1)
            h = 23
        else:
            if h%3==2: pass
            else: h = h - (h%3 + 1)
        fcst_time = time.replace(hour=h,minute=0,second=0,microsecond=0)
        if fcst_time == datetime.now().replace(minute=0, second=0, microsecond=0):
            if datetime.now().minute < 10: fcst_time = fcst_time + timedelta(hours=-3)
        return fcst_time

    def __get_baseTime_UltraSrtFcst(self, time):
        fcst_time = time.replace(minute=30,second=0,microsecond=0)
        if time.minute < 30: fcst_time = fcst_time + timedelta(hours=-1)
        if fcst_time == datetime.now().replace(minute=30, second=0, microsecond=0):
            if datetime.now().minute < 45: fcst_time = fcst_time + timedelta(hours=-1)
        return fcst_time

    def __get_baseTime_UltraSrtNcst(self, time):
        ncst_time = time.replace(minute=0,second=0,microsecond=0)
        if time.minute < 30: ncst_time = ncst_time + timedelta(hours=-1)
        if ncst_time == datetime.now().replace(minute=0, second=0, microsecond=0):
            if datetime.now().minute < 40: ncst_time = ncst_time + timedelta(hours=-1)
        return ncst_time