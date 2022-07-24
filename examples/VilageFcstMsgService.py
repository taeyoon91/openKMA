from openKMA import VilageFcstMsgService

KMA_API = VilageFcstMsgService(r'BdJLVP6Ht6Z41L%2B5lMY8Fzeyob4xWJwkdI2a%2BHZ6aN7yWYjS6n9DAUGSPGf%2FZXujsUFZ2r4XH4hs7UjQSILr%2Fw%3D%3D')

# 기상개황조회
stnId = 109 # 지역:서울·인천·경기도, 통보문 지점명:수도권(서울)
result = KMA_API.getWthrSituation(stnId)
print(result.items)

# 육상예보조회
regId = '11B20601'  # 지역:서울·인천·경기도, 통보문 지점명:수원
result = KMA_API.getLandFcst(regId)
print(result.items)

# 해상예보조회
regId = '12B10300'  # 지역:제주도앞바다, 통보문 지점명:제주도앞바다
result = KMA_API.getSeaFcst(regId)
print(result.items)
