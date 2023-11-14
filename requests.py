import requests
from bs4 import BeautifulSoup
import os
os.chdir("C:/Users/laksrgan/OneDrive - Keysight Technologies/Recordings/Projects/'/C5 Input for participants/domestic_visitors")
# Send a request to the website
response = requests.get("https://www.indiacensus.net/states/telangana")

# Parse the response from the website
soup = BeautifulSoup(response.content, "html.parser")

# Extract the data that you want from the parsed response
title = soup.title.text
body = soup.body.text

# Store the data in a desired format
with open("data.csv", "w") as f:
    f.write("title,body\n")
    f.write(f"{title},{body}\n")