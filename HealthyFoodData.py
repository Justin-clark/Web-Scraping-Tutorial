import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get("http://www.health.com/health/gallery/0,,20576053,00.html#chicken-breast-with-shaved-brussels-sprouts--0")
soup = BeautifulSoup(page.content, 'html.parser')

food = soup.find_all(class_="media-body clearfix")
for ft in food:
    food_title = ft.find("h2").get_text()

food_info = pd.DataFrame({
    "Food Title" : food_title[0]
})

print(food_info)
