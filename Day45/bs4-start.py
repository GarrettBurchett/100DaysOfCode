from bs4 import BeautifulSoup

with open("Day45/website.html", encoding='utf8') as website: 
    contents = website.read()

soup = BeautifulSoup(contents, 'html.parser')
# print(soup.title)
# print(soup.title.string) # Pulls the string value for <title>

# print(soup.prettify()) # Prints the html content in a indented and more readable form

# print(soup.p) # Prints the 1st <p> tag found in the html

all_anchor_tags = soup.find_all(name="a") # Returns a list of the all <a> tags in the html

# for tag in all_anchor_tags:
#     print(tag.getText()) # Returns the text in all anchor tags
#     print(tag.get("href")) # Returns all of the href values

heading = soup.find(name="h1", id="name")
# print(heading) # returns the 1st h1 tag with an id of "name"

section_heading = soup.find(name="h3", class_="heading") # Must use class_ for searching a specific class in html. class is reserved in Python for creating classes only.

company_url = soup.select_one(selector="p a") # selector = CSS selector. select_one returns the 1st element found with the criteria
print(company_url)

name = soup.select_one(selector="#name") 
print(name) # Returns the 1st html element with id="name".

headings = soup.select(".heading") # select will return all elements matching the searching criteria. In this case, a class of heading (Think CSS styling)
print(headings) # Returns a list of all html elements with class="heading"