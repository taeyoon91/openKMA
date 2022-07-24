from openKMA._common._common import *

class MidFcstInfoService: #기상청_중기예보 조회서비스
    def __init__(self, ServiceKey=''):
        self.ServiceKey	= ServiceKey

    def getMidFcst(self, stnId:int, tmFc:datetime, pageNo:int=1, numOfRows:int=999, dataType:str='XML'): #중기전망조회
        dataType = dataType.upper()
        tmFc = self.__get_tmFc(tmFc)

        url = f"{domain_KMA}/{self.__class__.__name__}/{inspect.stack()[0][3]}?serviceKey={self.ServiceKey}"
        payload = { 'pageNo'   : pageNo,
                    'numOfRows': numOfRows,
                    'dataType' : dataType,
                    'stnId'    : stnId,
                    'tmFc'     : tmFc.strftime("%Y%m%d%H%M")
        }

        response = request_to_kma(url, payload)
        if not isinstance(response, requests.models.Response):
            return ResponseKMA(payload, response, None, None, None, None, None)

        if dataType == 'XML':
            resultCode, resultMsg, items = transform_xml_to_dataframe(response)
        elif dataType == 'JSON':
            resultCode, resultMsg, items = transform_json_to_dataframe(response.json())

        if isinstance(items, pd.DataFrame):
            items['stnId'] = stnId
            items['tmFc']  = tmFc
            items.set_index('tmFc',inplace=True)
            items.index = pd.to_datetime(items.index)

        return ResponseKMA(payload, response.url, response, resultCode, resultMsg, dataType, items)

    def getMidLandFcst(self, regId, tmFc:datetime, pageNo=1, numOfRows=999, dataType='XML'): #중기육상예보조회
        dataType = dataType.upper()
        tmFc = self.__get_tmFc(tmFc)

        url = f"{domain_KMA}/{self.__class__.__name__}/{inspect.stack()[0][3]}?serviceKey={self.ServiceKey}"
        payload = { 'pageNo'   : pageNo,
                    'numOfRows': numOfRows,
                    'dataType' : dataType,
                    'regId'    : regId,
                    'tmFc'     : tmFc.strftime("%Y%m%d%H%M")
        }

        response = request_to_kma(url, payload)
        if not isinstance(response, requests.models.Response):
            return ResponseKMA(payload, response, None, None, None, None, None)
        
        if dataType == 'XML':
            resultCode, resultMsg, items = transform_xml_to_dataframe(response)
        elif dataType == 'JSON':
            resultCode, resultMsg, items = transform_json_to_dataframe(response.json())

        if isinstance(items, pd.DataFrame):
            dic = items.to_dict()
            items = pd.DataFrame()
            for n in range(3-1,10+2):
                if not ( f'rnSt{n}Am' in dic or f'rnSt{n}' in dic or \
                        f'wf{n}Am'   in dic or f'wf{n}'  in dic ): continue
                tmp = {'n_days_later': n , 
                    'Date'  : (tmFc + timedelta(days=+n)).date() }
                if f'rnSt{n}Am' in dic: tmp['rnStAm'] = dic[f'rnSt{n}Am']
                if f'rnSt{n}Pm' in dic: tmp['rnStPm'] = dic[f'rnSt{n}Pm']
                if f'rnSt{n}'   in dic: tmp['rnSt']   = dic[f'rnSt{n}']
                if f'wf{n}Am'   in dic: tmp['wfAm']   = dic[f'wf{n}Am']
                if f'wf{n}Pm'   in dic: tmp['wfPm']   = dic[f'wf{n}Pm']
                if f'wf{n}'     in dic: tmp['wf']     = dic[f'wf{n}']
                items = pd.concat([items, pd.DataFrame(tmp)])
            items['regId'] = regId
            items['tmFc'] = tmFc
            items.set_index('Date',inplace=True)
            items.index = pd.to_datetime(items.index)

        return ResponseKMA(payload, response.url, response, resultCode, resultMsg, dataType, items)
    
    def getMidTa(self, regId, tmFc:datetime, pageNo=1, numOfRows=999, dataType='XML'): #중기기온조회
        dataType = dataType.upper()
        tmFc = self.__get_tmFc(tmFc)

        url = f"{domain_KMA}/{self.__class__.__name__}/{inspect.stack()[0][3]}?serviceKey={self.ServiceKey}"
        payload = { 'pageNo'   : pageNo,
                    'numOfRows': numOfRows,
                    'dataType' : dataType,
                    'regId'    : regId,
                    'tmFc'     : tmFc.strftime("%Y%m%d%H%M")
        }

        response = request_to_kma(url, payload)
        if not isinstance(response, requests.models.Response):
            return ResponseKMA(payload, response, None, None, None, None, None)

        if dataType == 'XML':
            resultCode, resultMsg, items = transform_xml_to_dataframe(response)
        elif dataType == 'JSON':
            resultCode, resultMsg, items = transform_json_to_dataframe(response.json())

        if isinstance(items, pd.DataFrame):
            dic = items.to_dict()
            items = pd.DataFrame()
            for n in range(3-1,10+2):
                if not ( f'taMin{n}Low' in dic or f'taMin{n}' in dic or \
                        f'taMax{n}Low' in dic or f'taMax{n}' in dic): continue
                tmp = {'n_days_later': n , 
                    'Date'  : (tmFc + timedelta(days=+n)).date() }
                if f'taMin{n}Low'  in dic: tmp['taMinLow']  = dic[f'taMin{n}Low']
                if f'taMin{n}High' in dic: tmp['taMinHigh'] = dic[f'taMin{n}High']
                if f'taMin{n}'     in dic: tmp['taMin']     = dic[f'taMin{n}']
                if f'taMax{n}Low'  in dic: tmp['taMaxLow']  = dic[f'taMax{n}Low']
                if f'taMax{n}High' in dic: tmp['taMaxHigh'] = dic[f'taMax{n}High']
                if f'taMax{n}'     in dic: tmp['taMax']     = dic[f'taMax{n}']
                items = pd.concat([items, pd.DataFrame(tmp)])
            items['regId'] = regId
            items['tmFc']  = tmFc
            items.set_index('Date',inplace=True)
            items.index = pd.to_datetime(items.index)

        return ResponseKMA(payload, response.url, response, resultCode, resultMsg, dataType, items)
    
    def getMidSeaFcst(self, regId, tmFc:datetime, pageNo=1, numOfRows=999, dataType='XML'): #중기해상예보조회
        dataType = dataType.upper()
        tmFc = self.__get_tmFc(tmFc)

        url = f"{domain_KMA}/{self.__class__.__name__}/{inspect.stack()[0][3]}?serviceKey={self.ServiceKey}"
        payload = { 'pageNo'   : pageNo,
                    'numOfRows': numOfRows,
                    'dataType' : dataType,
                    'regId'    : regId,
                    'tmFc'     : tmFc.strftime("%Y%m%d%H%M")
        }

        response = request_to_kma(url, payload)
        if not isinstance(response, requests.models.Response):
            return ResponseKMA(payload, response, None, None, None, None, None)

        if dataType == 'XML':
            resultCode, resultMsg, items = transform_xml_to_dataframe(response)
        elif dataType == 'JSON':
            resultCode, resultMsg, items = transform_json_to_dataframe(response.json())

        if isinstance(items, pd.DataFrame):
            dic = items.to_dict()
            items = pd.DataFrame()
            for n in range(3-1,10+2):
                if not ( f'wh{n}AAm' in dic or f'wh{n}BAM' in dic or \
                        f'wh{n}A'   in dic or f'wf{n}Am'  in dic or \
                        f'wf{n}'    in dic ): continue
                tmp = {'n_days_later': n , 
                    'Date'  : (tmFc + timedelta(days=+n)).date() }
                if f'wh{n}AAm' in dic: tmp['whAAm'] = dic[f'wh{n}AAm']
                if f'wh{n}APm' in dic: tmp['whAPm'] = dic[f'wh{n}APm']
                if f'wh{n}BAm' in dic: tmp['whBAm'] = dic[f'wh{n}BAm']
                if f'wh{n}BPm' in dic: tmp['whBPm'] = dic[f'wh{n}BPm']
                if f'wh{n}A'   in dic: tmp['whA']   = dic[f'wh{n}A']
                if f'wh{n}B'   in dic: tmp['whB']   = dic[f'wh{n}B']
                if f'wf{n}Am'   in dic: tmp['wfAm'] = dic[f'wf{n}Am']
                if f'wf{n}Pm'   in dic: tmp['wfPm'] = dic[f'wf{n}Pm']
                if f'wf{n}'     in dic: tmp['wf']   = dic[f'wf{n}']
                items = pd.concat([items, pd.DataFrame(tmp)])
            items['regId'] = regId
            items['tmFc'] = tmFc
            items.set_index('Date',inplace=True)
            items.index = pd.to_datetime(items.index)

        return ResponseKMA(payload, response.url, response, resultCode, resultMsg, dataType, items)

    def __get_tmFc(self, time):
        time = time.replace(minute=0,second=0,microsecond=0)
        h = time.hour
        if   h >= 18: time = time.replace(hour=18)
        elif h >=  6: time = time.replace(hour= 6)
        else: time = ( time + timedelta(days=-1) ).replace(hour=18)
        
        return time