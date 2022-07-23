#from openKMA.core import *

import imp
import logging
from datetime import datetime, timedelta
import json

import requests
import xmltodict

import pandas as pd

domain_KMA = 'http://apis.data.go.kr/1360000'

class ResponseKMA:
    def __init__(self, parameters, url, response, resultCode, resultMsg, dataType, items):
        self.parameters = parameters
        self.url        = url
        self.response   = response
        self.resultCode = resultCode
        self.resultMsg  = resultMsg
        self.dataType   = dataType
        self.items      = items

def requests_to_kma(url, payload):
    for i in range(0,3):
        response = requests.get(url, params=payload)
        if 'Set-Cookie' in response.headers: return response

    logging.warning( f"""
    공공데이터포털(data.go.kr)이 제공기관(기상청)으로 부터
    데이터를 정상적으로 수신하지 못 하였습니다. 다음 응답을 참고해 주세요.
    -------------------------[공공데이터포털 응답]-------------------------
    {response.text}
    "-----------------------------------------------------------------------""" )

    return response.url

def transform_xml_to_dataframe(xml):
    xml2json = xmltodict.parse(xml.text)
    xml2json = json.dumps(xml2json)
    xml2json = json.loads(xml2json)
    return transform_json_to_dataframe(xml2json)

def transform_json_to_dataframe(json):
    resultCode = json['response']['header']['resultCode']
    resultMsg  = json['response']['header']['resultMsg']
    if resultCode != "00":
        logging.warning(f"제공기관(기상청)으로 부터 비정상적인 응답을 "\
                        f"수신하였습니다. 다음 응답메세지를 참고해 주세요.\n\n"\
                        f"{resultMsg}({resultCode})\n")
        return resultCode, resultMsg, None
    items = pd.json_normalize(json['response']['body']['items']['item'])
    return resultCode, resultMsg, items
