# ！ /usr/bin/python3
# -*-coding:UTF-8-*-

import requests
import pandas as pd
from bs4 import BeautifulSoup


def get_data():
    url = 'http://www.tmooc.cn/'
    headers = {'User-Agent': 'Mozilla/5.0(Windows NT 6.1;WOW64)'}
    data = requests.get(url, headers=headers)
    return data


def parse_data(data):
    soup = BeautifulSoup(data.text, 'lxml')

    books_left = soup.find('ul', {'class': 'cover-col-4 clearfix'})
    books_left = books_left.find_all('li')

    books_right = soup.find('ul', {'class': 'cover-col-4 pl20 clearfix'})
    books_right = books_right.find_all('li')

    books = list(books_left) + list(books_right)

    img_urls = []
    titles = []
    ratings = []
    authors = []
    details = []

    for book in books:
        img_url = book.find_all('a')[0].find('img').get('src')
        img_urls.append(img_url)

        title = book.find_all('a')[1].get_text()
        titles.append(title)

        rating = book.find('p', {'class': 'rating'}).get_text()
        rating = rating.replace('\n', '').replace(' ', '')
        ratings.append(rating)

        author = book.find_all('p', {'class': 'color-gray'}).get_text()
        author = author.replace('\n', '').replace(' ', '')
        authors.append(author)

        detail = book.find_all('p')[2].get_text()
        detail = detail.replace('\n', '').replace(' ', '')
        details.append(detail)

    print('img_urls:', img_urls)
    print('titles:', titles)
    print('ratings:', ratings)
    print('authors:', authors)
    print('details:', details)

    return img_urls, titles, ratings, authors, details


def save_data(img_urls, titles, ratings, authors, details):
    result = pd.DataFrame()
    result['img_urls'] = img_urls
    result['titles'] = titles
    result['ratings'] = ratings
    result['authors'] = authors
    result['details'] = details
    result.to_csv('result.csv', index=None)


def run():
    data = get_data()
    img_urls, titles, ratings, authors, details = parse_data(data)
    save_data(img_urls, titles, ratings, authors, details)


if __name__ == '__main__':
    run()
