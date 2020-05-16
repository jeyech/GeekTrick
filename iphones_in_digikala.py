import csv
import re
import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.digikala.com/search/category-mobile-phone/?has_selling_stock=1&q=%DA%AF%D9%88%D8%B4%DB%8C%20%D9%85%D9%88%D8%A8%D8%A7%DB%8C%D9%84%20%D8%A7%DB%8C%D9%81%D9%88%D9%86&pageno=1&sortby=22')
#faghat gushi haye mojood tu anbare digikala ro scrap mikone

soup = BeautifulSoup(r.text,'html.parser')

ip = soup.find_all('div' ,attrs = {'class':'c-product-box__content'})

d = open("iphones_output_file.csv","w")

for phone in ip: 
    d.write(re.sub(r'\s+',' ',phone.text))
    d.write('\n')

d.close()
