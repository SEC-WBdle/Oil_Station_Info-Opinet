![OPINET DOWNLOAD](https://github.com/SEC-WBdle/Oil_Station_Info-Opinet/blob/main/IMAGE/LESSON1.png)

# **전체 소스** 
* ![전체 소스](https://github.com/SEC-WBdle/Oil_Station_InfoOpinet/blob/main/CODE/%5BOpinet%20Download%5D%20%EC%8B%BC%20%EC%A3%BC%EC%9C%A0%EC%86%8C%20%EC%B0%BE%EA%B8%B0%20-%20%EC%A7%80%EC%97%AD%EB%B3%84%20.ipynb)


# **Step 별 소스**
![OPINET DOWNLOAD](https://github.com/SEC-WBdle/Oil_Station_Info-Opinet/blob/main/IMAGE/HOW%20TO%20(BY%20STEP).JPG)
# Oil_Station_Info-Opinet
  * Opinet(Oil_Station_Info) 오피넷 정보 Analysis


# STEP 1 - Install Libraries
```
!pip install selenium --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org
```
 *  ![자세한 소스파일(PY)]( https://github.com/SEC-WBdle/Oil_Station_Info-Opinet/blob/main/CODE/Step%201%20-%20Install%20Libraries%20(%EB%AA%A8%EB%93%88%20%EC%84%A4%EC%B9%98).py)
 

 # STEP 2 - Chrome Driver 설치 방법 
 * Chrome 버전 확인
 * 설정 - Chrome - Chrome 정보 - Chrome 버젼 확인
 * 버전 87.0.4280.88(공식 빌드) (64비트) -> version 87
 *  ![자세한 소스파일(PY)](  https://github.com/SEC-WBdle/Oil_Station_Info-Opinet/blob/main/CODE/Step%202%20-%20Install%20Chrome%20Driver(%20%ED%81%AC%EB%A1%AC%20%EB%93%9C%EB%9D%BC%EC%9D%B4%EB%B2%84%20%EC%84%A4%EC%B9%98).py)


 # Step 3 - Chrome Driver 통해 웹페이지 [Opinet,오피넷] 접속
 * 주유쇼 관련 정보 가져오기 
 * opinet - 유가정보 제공 | 한국석유공사 
 * https://www.opinet.co.kr/
 * ![자세한 소스파일(PY)](  https://github.com/SEC-WBdle/Oil_Station_Info-Opinet/blob/main/CODE/Step%203%20-%20Chrome%20Driver%20%ED%86%B5%ED%95%B4%20%EC%9B%B9%ED%8E%98%EC%9D%B4%EC%A7%80%20%5BOpinet%2C%EC%98%A4%ED%94%BC%EB%84%B7%5D%20%EC%A0%91%EC%86%8D.py)
 
  *  오피넷 접속 
  ```
  from selenium import webdriver
  driver = webdriver.Chrome("C:/Users/Sung/Downloads/chromedriver.exe")
  driver.get("http://www.opinet.co.kr")
  ```
  *  Headless Option
  IF BACKGROUND 에서 진행하고 싶다면 -- HEADLESS OPTION 이 필요 



# Step 4 - 웹페이져 section 별 접근경로

![OPINET WEBSITE](https://github.com/SEC-WBdle/Oil_Station_Info-Opinet)
![OPINET DOWNLOAD](https://github.com/SEC-WBdle/Oil_Station_Info-Opinet/blob/main/IMAGE/OPINET.JPG)


접근하고 싶은 곳의 코드를 실행 
EX. 싼 주유소 찾기 - 지역별에 들어가고 싶으면 코드 한줄만 실행하면 됨 
```
driver.execute_script("return goSubPage(0,0,99)") # 싼 주유소 찾기 - 지역별 
```
EX. 
* 싼 주유소 찾기 
```
driver.execute_script("return goSubPage(0,0,99)") # 싼 주유소 찾기 - 지역별  
```

* 국내유가통계
```
driver.execute_script("return goSubPage(1,0,0)") # 국내유가통계 - 주유소 - 평균판매가격 
```

* 유가관련정보
```
driver.execute_script("return goSubPage(2,0,99)") # 유가관련정보 - 국내유가동향
```

* 불법행위공표
```
driver.execute_script("return goSubPage(3,0,99)") # 불법행위공표 - 불법행위공표사항 
```

* 이용안내
```
driver.execute_script("return goSubPage(4,0,0)") # 이용안내 - 오피넷이란
```
 * ![자세한 소스파일(PY)](  https://github.com/SEC-WBdle/Oil_Station_Info-Opinet/blob/main/CODE/Step%204%20-%20%EC%9B%B9%ED%8E%98%EC%9D%B4%EC%A7%80%20section%20%EA%B2%BD%EB%A1%9C%EB%B3%84%20%EC%A0%91%EA%B7%BC.py)
 
 
# Step 5 - 싼 주유소 찾기 - 지역별 
```
driver.execute_script("return goSubPage(0,0,99)")
```
 * ![자세한 소스파일(PY)]( https://github.com/SEC-WBdle/Oil_Station_Info-Opinet/blob/main/CODE/Step%205%20-%20%EC%8B%BC%20%EC%A3%BC%EC%9C%A0%EC%86%8C%20%EC%B0%BE%EA%B8%B0%20-%20%EC%A7%80%EC%97%AD%EB%B3%84.py)

# Step 6- 지역별(시도군)정보 가져오기 
```
si_list_raw = driver.find_element_by_css_selector('#SIDO_NM0')  # '시/도'이름 가져오기 #SIDO_NM0
si_list = si_list_raw.find_elements_by_tag_name("option")  # 하위 option tag
si_names = [option.get_attribute("value") for option in si_list]  # '시/도'이름 가져오기
si_names.remove('')  # si_names_list에서 ''제거
```
 * ![자세한 소스파일(PY)]( https://github.com/SEC-WBdle/Oil_Station_Info-Opinet/blob/main/CODE/Step%206%20-%20%EC%A7%80%EC%97%AD%EB%B3%84(%EC%8B%9C%EB%8F%84%EA%B5%B0)%20%EC%A0%95%EB%B3%B4%20%EA%B0%80%EC%A0%B8%EC%98%A4%EA%B8%B0.py)


# Step 7 - 부가정보 및 버튼클릭 
```
self_y = driver.find_element_by_css_selector('#SELF_DIV_CD').click() # 셀프 선택
car_wash = driver.find_element_by_css_selector('#CWSH_YN').click() # 세차장 선택
```
 * ![자세한 소스파일(PY)]( https://github.com/SEC-WBdle/Oil_Station_Info-Opinet/blob/main/CODE/Step%207%20-%20%EB%B6%80%EA%B0%80%EC%A0%95%EB%B3%B4%20%EB%B0%8F%20%EB%B2%84%ED%8A%BC%ED%81%B4%EB%A6%AD.py)

# Step 8 - 조회 버튼 및 엑셀 저장 
```
# 조회 버튼 
xpath = """//*[@id="searRgSelect"]/span"""
element_sel_gu = driver.find_element_by_xpath(xpath).click()

# 엑셀 저장
xpath = """//*[@id="glopopd_excel"]/span"""
element_get_excel = driver.find_element_by_xpath(xpath).click()
```
 * ![자세한 소스파일(PY)](  https://github.com/SEC-WBdle/Oil_Station_Info-Opinet/blob/main/CODE/Step%208%20-%20%EC%A1%B0%ED%9A%8C%20%EB%B2%84%ED%8A%BC%20%EB%B0%8F%20%EC%97%91%EC%85%80%20%EC%A0%80%EC%9E%A5.py)


