# Title: Website Information Lookup.
# Author: Huzbi.
# Creation Date: 08/07/2023.
# Description: A simple Python script which fetches some basic info for user-entered URL and also show social links on that page.

import socket
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

url = input('Enter your URL: ')
parsed_url = urlparse(url)
hostname = parsed_url.hostname

ip_address = socket.gethostbyname(hostname)
response = requests.get(f'https://ipinfo.io/{ip_address}/json')

data = response.json()
country = data['country']

url_response = requests.get(url)
soup = BeautifulSoup(url_response.text, 'html.parser')
anchor_tags = soup.find_all('a')

print("BASIC INFORMATION:")
print(f"The IP address of the {url} is {ip_address}")
print(f"The Country where the IP address {ip_address} is located is {country}\n")

print("SOCIAL LINKS:")
for tag in anchor_tags:
    href = tag.get('href')
    if href:
        href_insta = href
        if 'instgram.com' in href:
            print(f"Found Instgram Link: {href_insta}")
        elif 'facebook.com' in href:
            href_fb = href
            print(f"Found Facebook Link: {href_fb}")
        elif 'twitter.com' in href:
            href_twitter = href
            print(f"Found Twitter Link: {href_twitter}")
        elif 'github.com' in href:
            href_github = href
            print(f"Found Github Link: {href_github}")
        elif 'discord' in href:
            href_discord = href
            print(f"Found Discord Link: {href_discord}")
