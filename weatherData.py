import requests

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.WuKputPwZmA")

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content,'html.parser')

# Extracting a single element from data

seven_day = soup.find(id="seven-day-forecast") # tag that holds the weather info

forecast_items = seven_day.find_all(class_="tombstone-container") # forecast for the seven days

tonight = forecast_items[0] # forecast for the first day

period = tonight.find(class_="period_name") # tag for tonight
short_desc = tonight.find(class_="short-desc") # tag with short description
temp = tonight.find(class_="temp") # tag with temperature

img = tonight.find("img") # extract img tag
desc = img['title'] # extract the 'title' from img tag

# Extracting all elements from data

period_tags = seven_day.select(".tombstone-container .period-name") # uses css selectors to select period names
periods = [pt.get_text() for pt in period_tags] # iterate through period tags which hold which day it is
# same method can be used to access their descriptions
short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

# now we use Pandas to analyze the data
import pandas as pd
weather = pd.DataFrame({ # we use the data frame class and pass in each list of items as a dictionary
    "periods" : periods,
    "short_desc" : short_desc,
    "temp" : temp,
    "desc" : desc
})

print(weather)
