import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')

titles = soup.find_all(name='h3', class_='title')

title_list = [title.getText() for title in titles]

with open('./Day45/movies.txt', 'w', encoding='utf8') as file:
    for title in reversed(title_list):
        file.write(title + '\n')