from bs4 import BeautifulSoup
import requests
#get the page
page=requests.get(url="https://news.ycombinator.com/")
#print(page.text)
content=page.text
#create soup
soup=BeautifulSoup(content,"html.parser")
#print(soup.prettify())
#select titleline class elements
elements=soup.select(selector=".titleline")
print(elements)
news_and_link={}
for element in elements:
    a=element.find(name="a")
    news_string=a.string
    news_link=a["href"]
    print("\n\n")
    print(f" news : {news_string}")
    print(f"link : {news_link}")
    #add news and link to a dictionary
    dict1={news_string:news_link}
    news_and_link.update(dict1)
#view the news and link dictionary
count=1
new_dictionary={}
for x in news_and_link.items():
    #print(x)
    #modify the values loopwise
    #new_news=input(f"enter news no {count} : \n")
    #new_link=input(f"enter link : \n")
    #key_value={new_news:new_link}
    #new_dictionary.update(key_value)
    pass
    count+=1
#view the new dictionary
for x in new_dictionary.items():
    print(x)
#get the points for the newsz items
points=soup.select(selector=".score")
points_list=[]
for point in points:
    print(f"point : {point}")
    point_string=point.string
    points_list.append(point_string)
points_value_list=[point.split(sep=" ")[0] for point in points_list]
print(points_value_list)

