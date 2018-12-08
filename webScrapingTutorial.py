import requests

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html") # requests the info from site
                                                                                   # using get function
from bs4 import BeautifulSoup # Beautiful Soup library
soup = BeautifulSoup(page.content, 'html.parser') # parses HTML code

soup.prettify() # shows nested HTML code

list(soup.children) # structure of the top using children, returns a list

[type(item) for item in list(soup.children)] # checks what type of element is in the list
                                             # the Tag element is important

html = list(soup.children)[2] # access the html tag which is the third element

list(html.children) # we can see the tags of the html

body = list(html.children)[3] # this is where the body tag is

list(body.children) # look for the p tag inside of the body

p = list(body.children)[1] # extracts the p tag

print(p.get_text()) # gets the text from the p tag

# Another way to search for a specific tag is find_all()

soup.find_all('p') # returns a list of all p tags

soup.find('p') # returns first instance of tag
