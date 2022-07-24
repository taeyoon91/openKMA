from openKMA import VilageFcstInfoService
from datetime import datetime, timedelta

KMA_API = VilageFcstInfoService(r'BdJLVP6Ht6Z41L%2B5lMY8Fzeyob4xWJwkdI2a%2BHZ6aN7yWYjS6n9DAUGSPGf%2FZXujsUFZ2r4XH4hs7UjQSILr%2Fw%3D%3D')

# 동네예보 지점 격자X, 격자Y
X = 59  # 서울특별시 동작구 
Y = 125 # 신대방동

basedatetime = datetime.now()

result = KMA_API.getFcstVersion('SHRT', basedatetime)
print(result.items)

result = KMA_API.getUltraSrtNcst(X, Y, basedatetime)
print(result.items)

result = KMA_API.getUltraSrtFcst(X, Y, basedatetime)
print(result.items)

result = KMA_API.getVilageFcst(X, Y, basedatetime)
print(result.items)

