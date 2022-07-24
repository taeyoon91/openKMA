from datetime import datetime, timedelta
from openKMA import TyphoonInfoService

KMA_API = TyphoonInfoService(r'BdJLVP6Ht6Z41L%2B5lMY8Fzeyob4xWJwkdI2a%2BHZ6aN7yWYjS6n9DAUGSPGf%2FZXujsUFZ2r4XH4hs7UjQSILr%2Fw%3D%3D')

toTmFc = datetime.now()
fromTmFc = toTmFc + timedelta(days=-2)

# 태풍정보조회
result = KMA_API.getTyphoonInfo(fromTmFc, toTmFc)

# 태풍정보목록조회
tmFc = datetime.now() + timedelta(days=-2)
result = KMA_API.getTyphoonInfoList(tmFc)

# 태풍예상정보조회
typSeq = 1 #태풍번호
result = KMA_API.getTyphoonFcst(typSeq, tmFc)