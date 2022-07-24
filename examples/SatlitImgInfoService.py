from openKMA import SatlitImgInfoService
from datetime import datetime, timedelta

KMA_API = SatlitImgInfoService(r'BdJLVP6Ht6Z41L%2B5lMY8Fzeyob4xWJwkdI2a%2BHZ6aN7yWYjS6n9DAUGSPGf%2FZXujsUFZ2r4XH4hs7UjQSILr%2Fw%3D%3D')

sat  = 'G2'   #천리안위성 2A호
data = 'rgbt' #RGB컬러
area = 'fd'
time = datetime.now() + timedelta(days=-1)

result = KMA_API.getInsightSatlit(sat, data, area, time)
print(result.items)