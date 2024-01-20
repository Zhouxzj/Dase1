import requests
from bs4 import BeautifulSoup
import csv

# url for sina news worlds
url = 'https://news.sina.com.cn/world/'
# send request and get the data
response = requests.get(url)
response.encoding = 'utf-8'
# parse html
soup = BeautifulSoup(response.text, 'html.parser')
# find news list
news_list = soup.find_all('div', class_='news-item')
# list for saving data
news_data = []
# browse all lists, get what we want
for news in news_list:
    title_tag = news.find('h2')
    if title_tag:
        title = title_tag.get_text().strip()
        link = title_tag.find('a')['href']
        time_tag = news.find('div', class_='time')
        # print(title)
        news_time = time_tag.get_text().strip()
        news_data.append([title, news_time, link])
# save filtered data in csv
with open('sina.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['标题', '时间', '链接'])
    for item in news_data:
        writer.writerow(item)
