# gedit fk-web-s.py
import requests 
import sys 
from bs4 import BeautifulSoup 
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
# driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
# products=[] #List to store name of the product
# prices=[] #List to store price of the product
# ratings=[] #List to store rating of the product
# driver.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;uniq")
# content = driver.page_source
# soup = BeautifulSoup(content)
# for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
#  name=a.find('div', attrs={'class':'_3wU53n'})
#  price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
#  rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
#  products.append(name.text)
#  prices.append(price.text)
#  ratings.append(rating.text)
# df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
# df.to_csv('products.csv', index=False, encoding='utf-8')


payload = {'q':'laptop'} 
r = requests.get('http://www.flipkart.com/search', params = payload) 
data = r.content.decode(encoding='UTF-8') 
f = open("flipkartdata.txt","w+",encoding='UTF-8') 
f.write(data)
soup = BeautifulSoup(r.content.decode(encoding='UTF-8'), "lxml")
collection = soup.find_all("div", {"class": "_2kHMtA"})#input your class of the required search
href = []
for c in collection:
 a = c.find("a")
 href.append(a['href'])
 #can store the data as such you want
