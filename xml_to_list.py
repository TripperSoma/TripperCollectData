import urllib .request
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import parse, Element
import numpy as np

def query_sender(data_sid):#, timecode):
    #url address
    url = 'http://apis.data.go.kr/6260000/BusanTourInfoService/getLuxuryTourDetail'
    #service key
    key = urllib.parse.unquote('P1c4m2lUvkf3mlKVA9W%2BGq6Di3Gs1HiMcyx9HukfeFP8Q7hVJ%2FNJ0u1EFiB7ql728phCz8%2Fc3R6hmPjPbEMeqA%3D%3D')
    #code = urllib.parse.unquote(categoryname)
    queryParams = '?' + urllib.parse.urlencode({ urllib.parse.quote_plus('ServiceKey') :key, urllib.parse.quote_plus('data_sid') : data_sid})#,urllib.parse.quote_plus('resultCode') : '1' })

    
    request = urllib.request.Request(url+ queryParams)#+code_info+key)
    request.get_method = lambda: 'GET'
    response_body = urllib.request.urlopen(request).read()
    u = str(response_body, "utf-8")
    return u


import xml.etree.ElementTree as ET


def xml_to_item_list(xml_string,data_sid):
    
    result = []
    root = ET.fromstring(xml_string)
    elements = root.findall('body/items/item')
    for item in elements:
        try:
            item_list = []
            item_list.append(data_sid)
            item_list.append(item.find('addr').text)
            item_list.append(item.find('dataTitle').text)
            #item_list.append(item.find('dataContent').text)
            item_list.append(item.find('wgsx').text)
            item_list.append(item.find('wgsy').text)
            result.append(item_list)
        except Exception as e:
            print("This row will be ignored. ",item_list)            
    return result

#item_list = xml_to_item_list(xml_string,'1')
#print(item_list)


from pprint import pprint

#item_numpy_list = np.array(item_list)

import pandas as pd


import csv



def numpy_to_csv(item_list):
##    pda = pd.DataFrame(item_list)
##    pda.to_csv("mylist.csv")
##    
    #df = pd.DataFrame(item_numpy_list)
    #print(item_numpy_list)
    #df.to_csv("tmp.csv",encoding='utf8', header = False, index = False)
    
    f = open('output.csv', 'w', encoding='utf8', newline='')
    wr = csv.writer(f)
    for sublist in item_list:
        for line in sublist:
            wr.writerow(line)
    f.close()
    
total_list=[]
                    
def item_writer(data_sid):
    xml_string = query_sender(data_sid)
    item_list = xml_to_item_list(xml_string,data_sid)
    total_list.append(item_list)

for i in range(4):
    item_writer(i)

numpy_to_csv(total_list)

