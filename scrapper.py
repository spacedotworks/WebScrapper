#!/usr/bin/python
from urllib2 import urlopen
from bs4 import BeautifulSoup

def run(code,page):
#    url = "http://www.kakuyasu.co.jp/ec/disp/CSfDispListPage_001.jsp?action=&dispNo=00"+ str(code) +"&q=&j=&min=&max=&ys=&yl=&yoryotanni=&allSearch=&type=01&sort=01&page=" + str(page)
    url = "https://www.aeonshop.com/shop/r/r08_p2_n01050000059020/"

#    req = urllib2.Request(url, headers={ 'User-Agent': 'Mozilla/5.0' })
#    html = urllib2.urlopen(req).read()
#    print url
    html = urlopen(url)
    soup = BeautifulSoup (html)

    for data in soup.find_all('a'):
        if data.parent.name == "div":
            text = data.text
#            with open("aeon.txt", "a") as myfile:
#                myfile.write(text.encode('utf-8'))
            #print (text)

for code in range (1, 2):
    for page in range(1,2):
        print code
        print page 
        run(code,page)
