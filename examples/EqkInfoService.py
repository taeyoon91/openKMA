from datetime import datetime, timedelta
from openKMA import EqkInfoService

KMA_API = EqkInfoService(r'BdJLVP6Ht6Z41L%2B5lMY8Fzeyob4xWJwkdI2a%2BHZ6aN7yWYjS6n9DAUGSPGf%2FZXujsUFZ2r4XH4hs7UjQSILr%2Fw%3D%3D')
toTmFc = datetime.now()
fromTmFc = toTmFc + timedelta(days=-2)

# 지진통보문조회
result = KMA_API.getEqkMsg(fromTmFc, toTmFc)
print(result.items)

# 지진통보문 목록조회
result = KMA_API.getEqkMsgList(fromTmFc, toTmFc)
print(result.items)

# 지진해일통보문조회
result = KMA_API.getTsunamiMsg(fromTmFc, toTmFc)
print(result.items)

# 지진해일통보문 목록조회
result = KMA_API.getTsunamiMsgList(fromTmFc, toTmFc)
print(result.items)
