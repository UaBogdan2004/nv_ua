import cloudscraper
from bs4 import BeautifulSoup
import csv
import time
import random
import json
scraper = cloudscraper.create_scraper()
news_list = []

with open('news.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Link', 'Date'])
    for item in range(1, 100):
        url = f'https://nv.ua/ukr/ukraine.html?page={item}'
        r = scraper.get(url)

        soup = BeautifulSoup(r.text, 'lxml')
        cards = soup.find_all(class_='row-result')

        for card in cards:
            name_news = card.find(class_='title')
            link_news = card.find(class_='row-result-body')['href']
            date_news = card.find(class_='additional-pub-date')
            print(f'{name_news.text.strip()} : {link_news} : {date_news.text.strip()}')
            writer.writerow([name_news.text.strip(), link_news, date_news.text.strip()])

            news_list.append({
                'Title': name_news.text.strip(),
                'Link': link_news,
                'Date': date_news.text.strip(),
            })
        time.sleep(random.uniform(1, 3))

with open('news.json', 'w') as file:
    json.dump(news_list, file, indent=4, ensure_ascii=False)