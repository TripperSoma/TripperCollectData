from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys
import io
from selenium.webdriver.common.action_chains import ActionChains
import csv
import pandas


browser = webdriver.Chrome('/Users/jhmon/Downloads/chromedriver')
#browser.get('https://www.google.com/maps/place/Embassy+Manyata+Business+Park/@13.0499862,77.6175589,17z/data=!3m1!4b1!4m10!1m2!2m1!1smanyata+tech+park+banglore!3m6!1s0x3bae176ddc662065:0x57b2874f9023bb8!8m2!3d13.049981!4d77.6197476!9m1!1b1')
browser.get('https://www.google.com/maps/contrib/104457113463029336984/reviews/@35.7355773,129.1157881,9z?hl=ko-KR')
actions = ActionChains(browser)

browser.maximize_window()
time.sleep(3)
#content = browser.find_element_by_class_name('scrollable-show').click()
htmlstring = browser.page_source
afterstring=""
for _ in range(10000):
    afterstring = htmlstring
    actions.send_keys(Keys.PAGE_DOWN).perform()
    htmlstring = browser.page_source
    if afterstring == htmlstring:
        print ("ended scraping crack test one")
        actions.send_keys(Keys.PAGE_DOWN).perform()
        htmlstring = browser.page_source
        if afterstring == htmlstring:
           print ("--Scrapping End--")
           break
    time.sleep(3)
    
#print(htmlstring)
item =[]

csvFile = io.open("user_review_data.csv",'w+',encoding='utf-8',newline='')
try :
    writer = csv.writer(csvFile)
    writer.writerow(('user','trip','rating','review'))
    #for i in range(20):
    #    writer.writerow((i,i+2,i*2))
    #print("yes?")
finally:
    csvFile.close()

#svFile = open("user_review_data.csv",'w+',encoding='utf-8',newline='')
#textdoc = io.open("gmapreview.txt", "w", encoding="utf-8")
soup = BeautifulSoup(htmlstring,"lxml")
mydivs = soup.findAll("div", {"class": "section-review-content"})
counter = 0

for a in mydivs:
    temp=[]
    temp.append(a.find(".section-review-title-consistent-with-review-text span"))#.text)
    print(a.select(".section-review-titles span")[3].text)
    print(a.select(".section-review-titles span")[4].text)

    
    #temp.append(a.find("div", class_="section-review-subtitle.section-review-subtitle-nowrap").text)#.text)
    #temp.append(a.find("a").get('href'))
    #writer.writerow(str("\nReviewer name: "+a.find("div", class_="section-review-title").text)," \n||Reviewer Detail: " + str(a.find("div", class_="section-review-subtitle").text) ," \n||Reviewerer Profile URL:"+str(a.find("a").get('href')))

    #temp.append(a.find("span", class_="section-review-text").text)
    #temp.append(a.find("span", class_="section-review-publish-date").text)
    # temp.append(a.find("span aria-label",class_="section-review-stars").text)
    print(a.find("span",class_="section-review-stars")['aria-label'])
    #writer.writerow(" \n||" + a.find("span", class_="section-review-text").text," \n|| " + a.find("span", class_="section-review-publish-date").text ," \n|| "+ a.find("span",class_="section-review-stars").text)
    #writer.write("=========================================\n")
    counter = counter + 1
    item.append(temp)
    
#print(item)

#data processing works
data=pandas.DataFrame(item)
data.to_csv('review_ratings.csv',encoding='cp949')
print ("Total reviews scraped:"+str(counter))
#textdoc.close()
#writer.close()
    
#actions.send_keys(Keys.PAGE_DOWN).perform()

#browser.execute_script('')
