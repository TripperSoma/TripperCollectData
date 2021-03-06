from urllib.parse import quote
from urllib.request import Request, urlopen
import ssl
import json
 
 
name = quote('부산시')   
API_KEY='AIzaSyCO8Qwx7jM2MDSgujwE-l9lYbwgTvgCUc0'

def build_addr(name):
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address='+ name+',rating' +'&key='+API_KEY+'&language=ko'
    req = Request(url, headers={ 'X-Mashape-Key': API_KEY })
    ssltext = ssl.SSLContext(ssl.PROTOCOL_TLSv1) 
    company_addr_json = urlopen(req, context=ssltext).read().decode('utf8')
    addr = json.loads(company_addr_json)
    return addr

def seperate_addr(addr):

    addr_detail= addr['results'][0]
    #전체 주소
    full_addr = addr_detail['formatted_address']
    #시도 주소
    city_addr1 = addr_detail['address_components'][4]['long_name']
    #구 주소
    city_addr = addr_detail['address_components'][3]['long_name']
    #동,읍 주소
    go_addr = addr_detail['address_components'][2]['long_name'] 
    #대로 주소
    dong_addr = addr_detail['address_components'][1]['long_name']
    #번지 주소
    bunji_addr = addr_detail['address_components'][0]['long_name']
    place_id = addr_detail['place_id']
    return place_id

def get_place_id(addr):
    addr_detail= addr['results'][0]
    place_id=addr_detail['place_id']
    return place_id

def get_rating(place_id):
    rating_url = 'https://maps.googleapis.com/maps/api/place/details/json?placeid='+place_id+'&fields=name,rating,formatted_phone_number&key=AIzaSyCO8Qwx7jM2MDSgujwE-l9lYbwgTvgCUc0'
    req = Request(rating_url, headers={ 'X-Mashape-Key': 'AIzaSyCO8Qwx7jM2MDSgujwE-l9lYbwgTvgCUc0' })
    ssltext = ssl.SSLContext(ssl.PROTOCOL_TLSv1) 
    company_addr_json = urlopen(req, context=ssltext).read().decode('utf8')
    addr = json.loads(company_addr_json)
    print(addr)
    try:
        addr_rating= addr['result']['rating']
    except KeyError :
        addr_rating = 0
        
    return addr_rating


print(build_addr(name))
print(get_place_id(build_addr(name)))
print(get_rating(get_place_id(build_addr(name))))
##print(addr)
##print(place_id)
##print(rating_url)
##print(addr_rating)
###rating
###rating = addr['results'][1]
###print(rating)
##print(full_addr)
##print(city_addr1)
##print(city_addr)
##print(go_addr)
##print(dong_addr)
##print(bunji_addr)
