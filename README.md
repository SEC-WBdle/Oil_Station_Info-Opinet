![OPINET DOWNLOAD](https://github.com/SEC-WBdle/Oil_Station_Info-Opinet/blob/main/IMAGE/LESSON1.png)



# Oil_Station_Info-Opinet
  * Opinet(Oil_Station_Info) 오피넷 정보 Analysis


# STEP 1 - Install Libraries
```
!pip install selenium --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org
```
 * (https://github.com/SEC-WBdle/Oil_Station_Info-Opinet/blob/main/CODE/Step%201%20-%20Install%20Libraries%20(%EB%AA%A8%EB%93%88%20%EC%84%A4%EC%B9%98).py)
 

# STEP 2 - Chrome Driver 설치 방법 
 * Chrome 버전 확인
 * 설정 - Chrome - Chrome 정보 - Chrome 버젼 확인
 * 버전 87.0.4280.88(공식 빌드) (64비트) -> version 87
 * (https://github.com/SEC-WBdle/Oil_Station_Info-Opinet/blob/main/CODE/Step%202%20-%20Install%20Chrome%20Driver(%20%ED%81%AC%EB%A1%AC%20%EB%93%9C%EB%9D%BC%EC%9D%B4%EB%B2%84%20%EC%84%A4%EC%B9%98).py)


# Step 3 - Chrome Driver 통해 웹페이지 [Opinet,오피넷] 접속
 * 주유쇼 관련 정보 가져오기 
 * opinet - 유가정보 제공 | 한국석유공사 
 * https://www.opinet.co.kr/
 
 * 자세한 소스 - (https://github.com/SEC-WBdle/Oil_Station_Info-Opinet/blob/main/CODE/Step%203%20-%20Chrome%20Driver%20%ED%86%B5%ED%95%B4%20%EC%9B%B9%ED%8E%98%EC%9D%B4%EC%A7%80%20%5BOpinet%2C%EC%98%A4%ED%94%BC%EB%84%B7%5D%20%EC%A0%91%EC%86%8D.py)

  # 오피넷 접속 
  ```
  from selenium import webdriver
  driver = webdriver.Chrome("C:/Users/Sung/Downloads/chromedriver.exe")
  driver.get("http://www.opinet.co.kr")
  ```

  # Headless Option
  IF BACKGROUND 에서 진행하고 싶다면 -- HEADLESS OPTION 이 필요 


# 웹페이져 section 별 접근경로

![OPINET WEBSITE](https://github.com/SEC-WBdle/Oil_Station_Info-Opinet)

![OPINET DOWNLOAD](https://github.com/SEC-WBdle/Oil_Station_Info-Opinet/blob/main/IMAGE/OPINET.JPG)


접근하고 싶은 곳의 코드를 실행 
EX. 싼 주유소 찾기 - 지역별에 들어가고 싶으면 코드 한줄만 실행하면 됨 
```
driver.execute_script("return goSubPage(0,0,99)") # 싼 주유소 찾기 - 지역별 
```

* 싼 주유소 찾기 
```
driver.execute_script("return goSubPage(0,0,99)") # 싼 주유소 찾기 - 지역별  
driver.execute_script("return goSubPage(0,1,99)") # 싼 주유소 찾기 - 경로별
driver.execute_script("return goSubPage(0,2,99)") # 싼 주유소 찾기 - 도로별 
driver.execute_script("return goSubPage(0,3,99)") # 싼 주유소 찾기 - 면세유 
```

* 국내유가통계
```
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
```

* 유가관련정보
```
driver.execute_script("return goSubPage(2,0,99)") # 유가관련정보 - 국내유가동향
driver.execute_script("return goSubPage(2,1,0)") # 유가관련정보 - 원유
driver.execute_script("return goSubPage(2,1,1)") # 유가관련정보 - 석유제품
driver.execute_script("return goSubPage(2,1,2)") # 유가관련정보 - OECD
driver.execute_script("return goSubPage(2,2,99)") # 유가관련정보 - 전자상거래
driver.execute_script("return goSubPage(2,3,99)") # 유가관련정보 - 유류세
driver.execute_script("return goSubPage(2,4,99)") # 유가관련정보 - 단위환산표
driver.execute_script("return goSubPage(2,5,99)") # 유가관련정보 - 유가정보 API
```

* 불법행위공표
```
driver.execute_script("return goSubPage(3,0,99)") # 불법행위공표 - 불법행위공표사항 
driver.execute_script("return goSubPage(3,1,99)") # 불법행위공표 - 공표취소사항
```

* 이용안내
```
driver.execute_script("return goSubPage(4,0,0)") # 이용안내 - 오피넷이란
driver.execute_script("return goSubPage(4,0,1)") # 이용안내 - 가격조사 및 공개기준
driver.execute_script("return goSubPage(4,1,99)") # 이용안내 - 공지사항
driver.execute_script("return goSubPage(4,2,99)") # 이용안내 - 오피넷 스타트업 
driver.execute_script("return goSubPage(4,3,99)") # 이용안내 - 자주묻는질문
driver.execute_script("return goSubPage(4,4,99)") # 이용안내 - 사이트맵
```
