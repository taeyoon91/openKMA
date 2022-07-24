from datetime import datetime, timedelta
from openKMA import WthrWrnInfoService

KMA_API = WthrWrnInfoService(r'BdJLVP6Ht6Z41L%2B5lMY8Fzeyob4xWJwkdI2a%2BHZ6aN7yWYjS6n9DAUGSPGf%2FZXujsUFZ2r4XH4hs7UjQSILr%2Fw%3D%3D')

stnId = 133
toTmFc   = datetime.now()
fromTmFc = toTmFc + timedelta(days=-5)

#기상특보목록조회
result = KMA_API.getWthrWrnList(stnId, fromTmFc, toTmFc)
print(result.items)

#기상특보통보문조회
result = KMA_API.getWthrWrnMsg(stnId, fromTmFc, toTmFc)
print(result.items)

#기상정보목록조회
result = KMA_API.getWthrInfoList(stnId, fromTmFc, toTmFc)
print(result.items)

#기상정보문조회
result = KMA_API.getWthrInfo(stnId, fromTmFc, toTmFc)
print(result.items)

#기상속보목록조회
result = KMA_API.getWthrBrkNewsList(stnId, fromTmFc, toTmFc)
print(result.items)

#기상속보조회
result = KMA_API.getWthrBrkNews(stnId, fromTmFc, toTmFc)
print(result.items)

#기상예비특보목록조회
result = KMA_API.getWthrPwnList(stnId, fromTmFc, toTmFc)
print(result.items)

#기상예비특보조회
result = KMA_API.getWthrPwn(stnId, fromTmFc, toTmFc)
print(result.items)

#특보코드조회
warningType = 12 #폭염
areaCode    = 'L1030100' #대전광역시
result = KMA_API.getPwnCd(stnId, warningType, areaCode, fromTmFc, toTmFc)
print(result.items)

#특보현황조회
result = KMA_API.getPwnStatus()
print(result.items)
