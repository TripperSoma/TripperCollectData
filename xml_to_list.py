import urllib .request
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import parse, Element
import numpy as np
from urllib.parse import quote
import sys
from pprint import pprint

#item_numpy_list = np.array(item_list)

import pandas as pd


import csv


#export library
import maps_api


API_KEY='AIzaSyCO8Qwx7jM2MDSgujwE-l9lYbwgTvgCUc0'

def query_sender(category,data_sid):#, timecode):
    #url address
    url = 'http://apis.data.go.kr/6260000/BusanTourInfoService/'+category
    #service key
    key = urllib.parse.unquote('P1c4m2lUvkf3mlKVA9W%2BGq6Di3Gs1HiMcyx9HukfeFP8Q7hVJ%2FNJ0u1EFiB7ql728phCz8%2Fc3R6hmPjPbEMeqA%3D%3D')# urllib.parse.quote_plus('data_sid') : data_sid
    #code = urllib.parse.unquote(categoryname)
    queryParams = '?' + urllib.parse.urlencode({ urllib.parse.quote_plus('ServiceKey') :key, urllib.parse.quote_plus('data_sid') : data_sid})#,urllib.parse.quote_plus('resultCode') : '1' })

    
    request = urllib.request.Request(url+ queryParams)#+code_info+key)
    request.get_method = lambda: 'GET'
    response_body = urllib.request.urlopen(request).read()
    u = str(response_body, "utf-8")
    print(u)
    return u


import xml.etree.ElementTree as ET

def getThemeTourDetail(item_list):
    #505
    f = open('getThemeTourDetail.csv', 'w', encoding='utf8', newline='')
    wr = csv.writer(f)
    for sublist in item_list:
        for line in sublist:
            wr.writerow(line)
    f.close()
def getExperienceTourDetail(item_list):
    #18629
    f = open('getExperienceTourDetail.csv', 'w', encoding='utf8', newline='')
    wr = csv.writer(f)
    for sublist in item_list:
        for line in sublist:
            wr.writerow(line)
    f.close()
def getWalkingTourDetail(item_list):
    #461
    f = open('getWalkingTourDetail.csv', 'w', encoding='utf8', newline='')
    wr = csv.writer(f)
    for sublist in item_list:
        for line in sublist:
            wr.writerow(line)
    f.close()

def getTouristAttDetail(item_list):
    #485
    f = open('getTouristAttDetail.csv', 'w', encoding='utf8', newline='')
    wr = csv.writer(f)
    for sublist in item_list:
        for line in sublist:
            wr.writerow(line)
    f.close()
def getShoppingAttrDetail(item_list):
    #914
    f = open('getShoppingAttrDetail.csv', 'w', encoding='utf8', newline='')
    wr = csv.writer(f)
    for sublist in item_list:
        for line in sublist:
            wr.writerow(line)
    f.close()

def getSportsDetail(item_list):
    #10028
    f = open('getSportsDetail.csv', 'w', encoding='utf8', newline='')
    wr = csv.writer(f)
    for sublist in item_list:
        for line in sublist:
            wr.writerow(line)
    f.close()
def getRestaurantDetail(item_list):
    #10028
    f = open('getRestaurantDetail.csv', 'w', encoding='utf8', newline='')
    wr = csv.writer(f)
    for sublist in item_list:
        for line in sublist:
            wr.writerow(line)
    f.close()
def getLuxuryTourDetail(item_list):
    f = open('getLuxuryTourDetail.csv', 'w', encoding='utf8', newline='')
    wr = csv.writer(f)
    for sublist in item_list:
        for line in sublist:
            wr.writerow(line)
    f.close()
def xml_list(xml_string,data_sid,num):
    #
    print(xml_string)
    result = []
    root = ET.fromstring(xml_string)
    elements = root.findall('body/items/item')
    for item in elements:
        try:
            #item component
            #data sid // data_type //address // Title // dataContent // wgsx // wgsy // rating
            item_list = []
            item_list.append(data_sid)
            item_list.append(num)
            item_list.append(item.find('addr').text)
            item_list.append(item.find('dataTitle').text)
            search_name = item.find('addr').text + item.find('dataTitle').text
            #print(search_name)
            name = quote(search_name)
            item_list.append(item.find('dataContent').text)
            item_list.append(item.find('wgsx').text)
            item_list.append(item.find('wgsy').text)
            #print(maps_api.build_addr(name,API_KEY))
            #print(maps_api.build_addr(search_name))
            #print((maps_api.get_rating(maps_api.get_place_id(maps_api.build_addr(name,API_KEY)),API_KEY)))
            item_list.append(maps_api.get_rating(maps_api.get_place_id(maps_api.build_addr(name,API_KEY)),API_KEY))
            result.append(item_list)
        except Exception as e:
            print("This row will be ignored. ",item_list)            
    return result

#item_list = xml_to_item_list(xml_string,'1')
#print(item_list)





    

                    
def item_writer(category,data_sid,num):
    xml_string = query_sender(category,data_sid)
    item_list = xml_list(xml_string,data_sid,num)
    total_list.append(item_list)
    #print(item_list)




#getThemeTourDetail#505
 
#getExperienceTourDetail#18629
#getWalkingTourDetail#461
#getTouristAttDetail#485
#getShoppingAttrDetail#914
#getSportsDetail#10028
#getRestaurantDetail(total_list)#10028
#getLuxuryTourDetail

if __name__ == "__main__":
    total_list=[]
    num=1
    if(sys.argv[1]=='getThemeTourDetail'):
        max_len=505
        num=1
        for i in range(max_len):
            item_writer('getThemeTourDetail',i,num)
        getThemeTourDetail(total_list)
    elif (sys.argv[1]=='getExperienceTourDetail'):
        max_len=18629
        num=2
        for i in range(max_len):
            item_writer('getExperienceTourDetail',i,num)
        getExperienceTourDetail(total_list)
    elif(sys.argv[1]=='getWalkingTourDetail'):
        max_len=461
        num=3
        for i in range(max_len):
            item_writer('getWalkingTourDetail',i,num)
        getWalkingTourDetail(total_list)
    elif(sys.argv[1]=='getTouristAttDetail'):
        max_len=485
        num=4
        for i in range(max_len):
            item_writer('getTouristAttDetail',i,num)
        getTouristAttDetail(total_list)
    elif(sys.argv[1]=='getShoppingAttrDetail'):
        max_len=914
        num=5
        for i in range(max_len):
            item_writer('getShoppingAttrDetail',i,num)
        getShoppingAttrDetail(total_list)
    elif(sys.argv[1]=='getSportsDetail'):
        max_len=10#10028
        num=6
        for i in range(max_len):
            item_writer('getSportsDetail',i,num)
        getSportsDetail(total_list)
    elif(sys.argv[1]=='getRestaurantDetail'):
        max_len=2
        num=7
        #for i in range(max_len):
    #          item_writer('getRestaurantDetail',i,num)
        item_writer('getRestaurantDetail',461,num)
        getRestaurantDetail(total_list)
    elif(sys.argv[1]=='getLuxuryTourDetail'):
        max_len=300
        num=8
        for i in range(max_len):
            item_writer('getLuxuryTourDetail',i,num)
        getRestaurantDetail(total_list)

    

