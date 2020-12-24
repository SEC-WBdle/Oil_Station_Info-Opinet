#####################################
# 싼 주유소 찾기 - 지역별
# 형태 및 부가정보 click test
#####################################
# 충전소 section 선택
repair = driver.find_element_by_css_selector('#LPG_BTN').click() # 충전소 선택

# 형태 click
self_n = driver.find_element_by_css_selector('#NORM_YN').click() # 일반 선택
self_y = driver.find_element_by_css_selector('#SELF_DIV_CD').click() # 셀프 선택
fake = driver.find_element_by_css_selector('#VLT_YN').click() # 불법 선택
auth = driver.find_element_by_css_selector('#KPETRO_YN').click() # 인증 선택
pos = driver.find_element_by_css_selector('#KPETRO_DP_YN').click() # 전산 선택

# 부가정보 click
car_wash = driver.find_element_by_css_selector('#CWSH_YN').click() # 세차장 선택
repair = driver.find_element_by_css_selector('#MAINT_YN').click() # 경정비 선택
conv_store = driver.find_element_by_css_selector('#CVS_YN').click() # 편의점 선택
all247 = driver.find_element_by_css_selector('#SEL24_YN').click() # 24시간 선택