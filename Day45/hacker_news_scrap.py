from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')

articles = soup.find_all(name='span', class_='titleline') # soup.select_one('.titleline')
print(len(articles))
article_titles = [article.getText() for article in articles]
# print(article_titles)

article_links = [article.find('a').get('href') for article in articles]
# print(article_links)

article_upvotes = [int(score.getText().split()[0]) for score in soup.select('.score')]
print(article_upvotes)
print(len(article_upvotes))

difference = len(articles) - len(article_upvotes)

max_score = max(article_upvotes)
max_score_index = article_upvotes.index(max_score)

# max_score = 0
# max_score_index = 0
# for index, num in enumerate(article_upvotes):
#     if num > max_score:
#         max_score = num
#         max_score_index = index

print(article_titles[max_score_index + difference])
print(article_links[max_score_index + difference])
print(article_upvotes[max_score_index])

