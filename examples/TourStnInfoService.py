from datetime import datetime, timedelta
from openKMA import TourStnInfoService

KMA_API = TourStnInfoService(r'BdJLVP6Ht6Z41L%2B5lMY8Fzeyob4xWJwkdI2a%2BHZ6aN7yWYjS6n9DAUGSPGf%2FZXujsUFZ2r4XH4hs7UjQSILr%2Fw%3D%3D')

COURSE_ID = 390 #커플끼리 여행
CURRENT_DATE = datetime.now() + timedelta(days=-23)
HOUR = 24

# 동네예보조회
result = KMA_API.getTourStnVilageFcst(COURSE_ID, CURRENT_DATE, HOUR)
print(result.items)

# 기상지수예보조회
result = KMA_API.getTourStnWthrIdx(COURSE_ID, CURRENT_DATE, HOUR)
print(result.items)

# 시군구별관광기후지수조회
CITY_AREA_ID = '5013000000' #제주 서귀포시
DAY = 7
result = KMA_API.getCityTourClmIdx(CITY_AREA_ID, CURRENT_DATE, DAY)
print(result.items)