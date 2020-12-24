#####################################
# 싼 주유소 찾기 - 지역별
# 지역 - 시군구 선택 list 가져오기
#####################################

# <select style ="width:62px;" id ="SIDO_NM0" name= "SIDO_NM0"> == $0
#     <option value> 시/도 </option>
#     <option value ="서울특별시" selected = "selected"> 서울 </option>
#     <option value ="부산광역시"> 부산 </option>
#     <option value ="대구광역시"> 대구 </option>
#     <option value ="인천광역시"> 인천 </option>
#     <option value ="광주광역시"> 광주 </option>
#     <option value ="대전광역시"> 대전 </option> ........ 등

si_list_raw = driver.find_element_by_css_selector('#SIDO_NM0')  # '시/도'이름 가져오기 #SIDO_NM0
si_list = si_list_raw.find_elements_by_tag_name("option")  # 하위 option tag
si_names = [option.get_attribute("value") for option in si_list]  # '시/도'이름 가져오기
si_names.remove('')  # si_names_list에서 ''제거

# si_names # '서울특별시','부산광역시','대구광역시','인천광역시','광주광역시','대전광역시' 등

# <select style ="width:62px;" id ="SIGUNGU_NM0" name= "SIGUNGU_NM0"> == $0
#     <option value> 시/군/도 </option>
#     <option value ="강남구" selected = "selected"> 강남구 </option>
#     <option value ="강동구"> 강동구 </option>
#     <option value ="강북구"> 강북구 </option>
#     <option value ="강서구"> 강서구 </option>
#     <option value ="관악구"> 관악구 </option>
#     <option value ="광진구"> 광진구 </option> ........ 등
gu_list_raw = driver.find_element_by_css_selector("#SIGUNGU_NM0")  # '시/군/구'이름 가져오기 #SIDO_NM0
gu_list = gu_list_raw.find_elements_by_tag_name("option")  # 하위 option tag
gu_names = [option.get_attribute("value") for option in gu_list]  # 군구
gu_names.remove('')
# gu_names # 시가 서울특별시일때 , '강남구','강동구','강북구','강서구' 등