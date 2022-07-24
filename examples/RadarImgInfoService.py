from datetime import datetime, timedelta
from openKMA import RadarImgInfoService

KMA_API = RadarImgInfoService(r'BdJLVP6Ht6Z41L%2B5lMY8Fzeyob4xWJwkdI2a%2BHZ6aN7yWYjS6n9DAUGSPGf%2FZXujsUFZ2r4XH4hs7UjQSILr%2Fw%3D%3D')

time = datetime.now() + timedelta(days=-1)

result = KMA_API.getCmpImg(time)
print(result.items)

doc = 'KWK' #관악산(HSR)
result = KMA_API.getRadarIndvdlzImg(doc, time)
print(result.items)
print(result.url)
result.items.to_csv('test.csv')