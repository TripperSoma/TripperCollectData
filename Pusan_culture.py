#?serviceKey=4T6snsNlH5j6uf8iYxkWi3kzfsj8ApLieZligfpcOQD0dOvTyUrI%2BCvLpQSpOHvdH%2BwidnT6HW3xTVu7xIOT4w%3D%3D&category_code1=cour_01
##
##from urllib2 import Request, urlopen
##from urllib import urlencode, quote_plus
import urllib.request
url = 'http://apis.data.go.kr/6260000/BusanTourInfoService/getLuxuryTourList'
queryParams = '?' + urllib.parse.urlencode({ urllib.parse.quote_plus('ServiceKey') :
                                               '4T6snsNlH5j6uf8iYxkWi3kzfsj8ApLieZligfpcOQD0dOvTyUrI%2BCvLpQSpOHvdH%2BwidnT6HW3xTVu7xIOT4w%3D%3D',
                                               urllib.parse.quote_plus('category_code1') : 'cour_01' })

request = urllib.request.Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urllib.request.urlopen(request).read().decode('utf8')
print (response_body)



#response_body = urlopen(request).read()
