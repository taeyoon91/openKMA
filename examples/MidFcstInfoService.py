from openKMA import MidFcstInfoService
from datetime import datetime, timedelta

KMA_API = MidFcstInfoService(ServiceKey=r'BdJLVP6Ht6Z41L%2B5lMY8Fzeyob4xWJwkdI2a%2BHZ6aN7yWYjS6n9DAUGSPGf%2FZXujsUFZ2r4XH4hs7UjQSILr%2Fw%3D%3D')

tmFc = datetime.now()

# 중기기상전망조회
stnId = 133 # 대전, 세종, 충청남도
result = KMA_API.getMidFcst(stnId, tmFc)
print(result.items)

# 중기육상예보조회
regId = '11C20000' #대전, 세종, 충청남도
result = KMA_API.getMidLandFcst(regId, tmFc)
print(result.items)

# 중기해상예보조회
regId = '12B10500' #제주도
result = KMA_API.getMidSeaFcst(regId, tmFc)
print(result.items)

# 중기기온조회
regId = '11C20401' #대전
result = KMA_API.getMidTa(regId, tmFc)
print(result.items)