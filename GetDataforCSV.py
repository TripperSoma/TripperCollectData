
import urllib.request
import urllib.parse

decode_key = urllib.parse.unquote('P1c4m2lUvkf3mlKVA9W%2BGq6Di3Gs1HiMcyx9HukfeFP8Q7hVJ%2FNJ0u1EFiB7ql728phCz8%2Fc3R6hmPjPbEMeqA%3D%3D')  # decode 해줍니다.
url = 'http://apis.data.go.kr/6260000/BusanTourInfoService/getStayDetail'
queryParams = '?' + urllib.parse.urlencode({ urllib.parse.quote_plus('ServiceKey') :
                                               decode_key,
                                               urllib.parse.quote_plus('category_code1') : 'cour_01' })

request = urllib.request.Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urllib.request.urlopen(request).read().decode('utf8')
print (response_body)

##
##
##
##
##import urllib .request
##import xml.etree.ElementTree as ET
##from xml.etree.ElementTree import parse, Element
##
##def query_sender(localcode, timecode):
##    url = 'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade?'
##    code_info = 'LAWD_CD='+ localcode + '&DEAL_YMD=' + timecode
##    key = '&serviceKey=발급한 서비스키'
##    request = urllib.request.Request(url+code_info+key)
##    request.get_method = lambda: 'GET'
##    response_body = urllib.request.urlopen(request).read()
##    u = str(response_body, "utf-8")
##    return u
##
##
##def xml_to_item_list(xml_string,local_name, timecode):
##    result = []
##    root = ET.fromstring(xml_string)
##    elements = root.findall('body/items/item')
##    for item in elements:
##        try:
##            item_list = []
##            item_list.append(time_code)
##            item_list.append(item.find('거래금액').text)
##            item_list.append(item.find('건축년도').text)
##            item_list.append(local_name+" "+item.find('법정동').text+" "+item.find('지번').text)
##            item_list.append(item.find('아파트').text)
##            item_list.append(item.find('전용면적').text)
##            result.append(item_list)
##        except Exception as e:
##            print("This row will be ignored. ",item_list)            
##    return result


