import requests
from bs4 import BeautifulSoup
from lxml import etree
import time

base_url = ['https://aajtak.intoday.in/national.html','https://aajtak.intoday.in/world-news.html','https://aajtak.intoday.in/news-on-films.html'
           ,'https: // aajtak.intoday. in / business.html','https://aajtak.intoday.in/khabare-jara-hatke.html']
header = {"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"}


href = []
def each_item(base_url):
    index = 0
    global  href
    for i in range(3):
        index +=30
        ture_url = base_url+"/page/"+str(index)
        respond = requests.get(ture_url,headers=header).text
        content = etree.HTML(respond)
        for each in range(1,31):
            the_whole_url  = content.xpath('/html/body/li['+str(each)+']/div/a[1]')
            try :
                href.append(the_whole_url[0].attrib.get('href'))
            except IndexError:
                continue




article = ''
ti = 0
def catch_content(base_url,item):
    global article
    global ti
    ti +=1
    print("this is the",ti,"url")
    real_url = base_url+item
    respond = requests.get(real_url).content
    tree = etree.HTML(respond)
    try:
        time = tree.xpath('/html/body/section[2]/div/div/div/div/div[1]/div/div[1]/div[2]/div[1]/div/div[2]/p')[0].text
        article += time
        article += '\n'
        title = tree.xpath('/html/body/section[2]/div/div/div/div/div[1]/div/div[1]/div[1]/h1')[0].text
        article +=title
        content = tree.xpath('//div[@class = "detailTxtContainer storyBody middle_s adblockcontainer"]//p/text()')
        article +='\n'
        for text in content:
            article += text
            article += '\n'
        article +='\n' +'-----------------------------------------------------------------------------------'
    except IndexError:
        print("error")

each_item(base_url)

for i in href:
    catch_content(base_url,i)
    time.sleep(2)

with open('aajtak_hindi_news.txt','w',encoding='utf-8')as f:
    f.write(article)





