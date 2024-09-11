import sys
import json
import requests
from bs4 import BeautifulSoup
import figlet


# URL of the website you want to scrape
url = "http://www.figlet.org/fontdb.cgi"

# Use the requests library to fetch the content of the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Assuming font names are in <pre> tags (based on the structure of the page)
    # This is a simplistic approach; you might need to adjust the selector
    # based on the actual structure of the webpage and where the data resides.
    font_pre_tags = soup.find_all('pre')

    for pre_tag in font_pre_tags:
        # Assuming each font name is on its own line within a <pre> tag
        font_names = pre_tag.text.split('\n')

        # Print each font name
        for font_name in font_names:
            print(font_name)
else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")



#if sys.argv[1]=="--font" or sys.argv[1]=="-font" or sys.argv[2]==""
 #   sys.exit(")


