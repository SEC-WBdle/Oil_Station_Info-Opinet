#####################################
# 웹페이지 section 별 접근경로
#####################################
# javascript 로 실행

# 싼 주유소 찾기
driver.execute_script("return goSubPage(0,0,99)") # 싼 주유소 찾기 - 지역별
driver.execute_script("return goSubPage(0,1,99)") # 싼 주유소 찾기 - 경로별
driver.execute_script("return goSubPage(0,2,99)") # 싼 주유소 찾기 - 도로별
driver.execute_script("return goSubPage(0,3,99)") # 싼 주유소 찾기 - 면세유

# 국내유가통계
driver.execute_script("return goSubPage(1,0,0)") # 국내유가통계 - 주유소 - 평균판매가격
driver.execute_script("return goSubPage(1,0,1)") # 국내유가통계 - 주유소 - 면세유평균가격
driver.execute_script("return goSubPage(1,1,99)") # 국내유가통계 - 자동차/충전소
driver.execute_script("return goSubPage(1,2,99)") # 국내유가통계 - 유가 내려받기
driver.execute_script("return goSubPage(1,3,0)") # 국내유가통계 - 주간공급가격
driver.execute_script("return goSubPage(1,3,1)") # 국내유가통계 - 월간판매가격
driver.execute_script("return goSubPage(1,4,99)") # 국내유가통계 - 대리점
driver.execute_script("return goSubPage(1,5,99)") # 국내유가통계 - LPG 용기충전소
driver.execute_script("return goSubPage(1,6,99)") # 국내유가통계 - LPG 용기판매소
driver.execute_script("return goSubPage(1,7,99)") # 국내유가통계 - LPG 집단공급

# 유가관련정보
driver.execute_script("return goSubPage(2,0,99)") # 유가관련정보 - 국내유가동향
driver.execute_script("return goSubPage(2,1,0)") # 유가관련정보 - 원유
driver.execute_script("return goSubPage(2,1,1)") # 유가관련정보 - 석유제품
driver.execute_script("return goSubPage(2,1,2)") # 유가관련정보 - OECD
driver.execute_script("return goSubPage(2,2,99)") # 유가관련정보 - 전자상거래
driver.execute_script("return goSubPage(2,3,99)") # 유가관련정보 - 유류세
driver.execute_script("return goSubPage(2,4,99)") # 유가관련정보 - 단위환산표
driver.execute_script("return goSubPage(2,5,99)") # 유가관련정보 - 유가정보 API

# 불법행위공표
driver.execute_script("return goSubPage(3,0,99)") # 불법행위공표 - 불법행위공표사항
driver.execute_script("return goSubPage(3,1,99)") # 불법행위공표 - 공표취소사항

# 이용안내
driver.execute_script("return goSubPage(4,0,0)") # 이용안내 - 오피넷이란
driver.execute_script("return goSubPage(4,0,1)") # 이용안내 - 가격조사 및 공개기준
driver.execute_script("return goSubPage(4,1,99)") # 이용안내 - 공지사항
driver.execute_script("return goSubPage(4,2,99)") # 이용안내 - 오피넷 스타트업
driver.execute_script("return goSubPage(4,3,99)") # 이용안내 - 자주묻는질문
driver.execute_script("return goSubPage(4,4,99)") # 이용안내 - 사이트맵