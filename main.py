from bs4 import BeautifulSoup
with open("website.html") as file:
    content=file.read()
import requests
soup=BeautifulSoup(content ,"html.parser")
#getting hold of all h3 elements
headings=soup.findAll(name="h3")
print(headings)
#find headings with attributes
heading_class=soup.findAll(name="h1",id="name")
print(heading_class)
#get an attribute from the soup portion
for heading in headings:
    print(heading.get("class"))

#fetch all anchor tags
all_anchor_tags=soup.findAll(name="a")
for tag in all_anchor_tags:
    print(tag.get("href"))
#fetching the lists
lists=soup.find(name="ul")
print(lists)
#fetching by selection
company_url=soup.select_one(selector="p em strong a")
print(f"commpany =  {company_url.get('href')}")
#using the class and id selectors
with_class=soup.select(selector=".heading")
print(with_class)
#ids
with_id=soup.select(selector="#name")
print(with_id)

title2=soup.select(selector="body a")
print(f" title 2 : {[title.string for title in title2]}")
#accessing element attributes
#select the example
example=soup.select_one(selector=".example")
print(example.string)
#collect the link
print(f" link = {example['href']}")
#collect the id
print(f"id = {example.get('ids')}")
# TODO
#modifying attributes
example["href"]="www.google.com"
#print(example)
# todo FAMILIES
#identifying root element
soup_elements_list=[]
print("\n\n\n\n")
elements_list=["html","h1","h2","h3","h4","h5","h6","p","a","head","title","meta"]
for i in range(elements_list.__len__()):
    soup_elements_list.append(soup.findAll(name=elements_list[i]))
#print(soup_elements_list)
#access parent element
angela_link=soup.select_one(selector="p em strong a")
print(f"angela link {angela_link}")
#finding the parent element
parent=angela_link.parent
print(f"parent = {parent}")
#grandparent
grandparent=parent.parent.parent
print(f"grandparent = {grandparent}")
#finding grandparent sibling
siblings=grandparent.find_next_siblings()

siblings_list=list(siblings)

for x in siblings_list:
    print(x)
#finding if isleaf
def is_leaf(element):
    if element.findAll(recurseive=False):
        return False
    #empty tags
    
    if element.string is not None:
        return True
    return False


#finding children

child1=grandparent.children
print("\n\n\n")
print(f" parent : {grandparent}")
for child in soup.html.descendants:
    #distinguishing the string attributes
    if isinstance(child ,str):
        continue
    #removing leaves
    elif is_leaf(child):
        continue

    else:print(f"child : {child}")
print(f"children on recursive : {grandparent.em.strong.findAll(recursive=False)[0].string}")


