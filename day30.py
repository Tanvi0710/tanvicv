import requests
from bs4 import BeautifulSoup
import csv
errors=[]
dict={}
a=input("ENTER YOUR URL")
response=requests.get(a)
Soup=BeautifulSoup(response.content,"html.parser")
x=Soup.title.text
print(x)

if Soup.find(["h1","h2","h3","h4","h5","h6"]):
    print(Soup.find(["h1","h2","h3","h4","h5","h6"]))
    dict["heading"]="appropriate"
else:
    errors.append("headings not present")
    dict["heading"]="not appropriate"

if Soup.find("title"):
    print("title mentioned")
    dict["title"]="appropriate"
else:
    errors.append("title not mentioned")
    dict["title"]="not appropriate"

if len(x)<=5:
    print("appropriate")
    dict["title"]="appropriate"
else:
    errors.append("length of title not appropriate")
    dict["title"]="not appropriate"
# print(errors)

if Soup.find("meta",attrs={"name":"description"}):
    print("description present")
    dict["description"]="appropriate"
else:
    errors.append("description not mentioned")
    dict["description"]="not appropriate"

if Soup.find("meta",attrs={"name":"keywords"}):
    print("keywords present")
    dict["keywords"]="appropriate"
else:
    errors.append("keywords not mentioned")
    dict["keywords"]="not appropriate"
if Soup.find('img',attrs="alt"):
    print('present')
    dict['img alt']="approriate"
else:
    errors.append("img alt not present")
    dict["img alt"]="not appropriate"


print(errors)
print(dict)

