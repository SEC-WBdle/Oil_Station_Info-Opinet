#####################################
# 싼 주유소 찾기 - 지역별
# 조회 버튼 및 엑셀 저장
#####################################

# 조회 버튼
xpath = """//*[@id="searRgSelect"]/span"""
element_sel_gu = driver.find_element_by_xpath(xpath).click()

# 엑셀 저장
xpath = """//*[@id="glopopd_excel"]/span"""
element_get_excel = driver.find_element_by_xpath(xpath).click()