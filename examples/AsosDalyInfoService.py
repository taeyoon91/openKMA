from openKMA import AsosDalyInfoService
from datetime import datetime, timedelta

KMA_API = AsosDalyInfoService(r'BdJLVP6Ht6Z41L%2B5lMY8Fzeyob4xWJwkdI2a%2BHZ6aN7yWYjS6n9DAUGSPGf%2FZXujsUFZ2r4XH4hs7UjQSILr%2Fw%3D%3D')

stnIds    = 108 # 서울
startDtHh = datetime.strptime('2022-07-01', '%Y-%m-%d')
endDtHh   = datetime.strptime('2022-07-10', '%Y-%m-%d')

result = KMA_API.getWthrDataList(stnIds, startDtHh, endDtHh)

print(result.parameters)
print(result.url)
print(result.response)
print(result.resultCode)
print(result.resultMsg)
print(result.dataType)
print(result.items)