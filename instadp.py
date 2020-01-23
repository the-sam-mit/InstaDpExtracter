import os
import sys
import requests
import re
from bs4 import BeautifulSoup as bs
import shutil
import time

username = input('Enter username: ')

URL = "https://www.instagram.com/{}/".format(username)

response = requests.get(URL, verify = True)
# soup = BeautifulSoup(page.text, 'html.parser')
html = response.text 
bs_html = bs(html, features ="lxml") 
bs_html = bs_html.text 
index = bs_html.find('profile_pic_url_hd')+21
remaining_text = bs_html[index:] 
remaining_text_index = remaining_text.find('requested_by_viewer')-3
string_url = remaining_text[:remaining_text_index]
# print(string_url)
image_url =""
for i in range(0, len(string_url)):
	if string_url[i] == '\\':
		image_url = image_url + "&"
	elif i>=0 and string_url[i-1]!='\\' and string_url[i-2]!='\\' and string_url[i-3]!='\\' and string_url[i-4]!='\\' and string_url[i-5]!='\\' :	
		image_url = image_url + string_url[i]


# print(image_url)
user = "{}.jpg".format(username)
img_data = requests.get(image_url).content
with open(user, 'wb') as handler:
    handler.write(img_data)

print("Accepted:P")