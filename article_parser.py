# importing libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm


# get list of news articles from Aljazeera

def scrape_coverpage(coverpage_url, links=None):
    if links is None:
        links = []
    r = requests.get(coverpage_url)
    html = r.content
    # print(html)
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup.prettify())
    anchors = soup.find_all('a')

    for link in tqdm(anchors, desc="Parsing Cover Page"):
        # took all the new articles only
        prefix_2022 = "/news/2022"
        prefix_2021 = "/news/2021"
        if prefix_2022 in link.get('href') or prefix_2021 in link.get('href'):
            linkText = "https://aljazeera.com" + link.get('href')
            links.append(linkText)
            # print(linkText)


def article_parser(links=None):
    if links is None:
        links = []
    df = pd.DataFrame(columns=['Title', 'Subtitle', 'Date', 'Content'])
    title = []
    subtitle = []
    date = []
    content = []

    for link in tqdm(links, desc="Parsing Articles"):
        r = requests.get(link)
        article_page = r.content
        soup = BeautifulSoup(article_page, 'html.parser')
        # print(soup.find('div', {'class': 'wysiwyg wysiwyg--all-content css-1ck9wyi'}).get_text())
        # print("END OF ARTICLE")
        title.append(str(soup.find('h1').get_text()))
        subtitle.append(str(soup.find('em').get_text()))
        date.append(str(soup.find('span', {'aria-hidden': 'true'}).get_text()))
        content.append(str(soup.find('div', {'class': 'wysiwyg wysiwyg--all-content css-1ck9wyi'}).get_text()))
    df['Title'] = title
    df['Subtitle'] = subtitle
    df['Date'] = date
    df['Content'] = content

    return df


def data_proccesing(data):
    data['Title'] = data['Title'].str.encode("ascii", "ignore").str.decode('ascii')
    data['Title'] = data['Title'].str.replace(r'\n', ' ', regex=True)
    data['Title'] = data['Title'].str.strip()

    data['Subtitle'] = data['Subtitle'].str.encode("ascii", "ignore").str.decode('ascii')
    data['Subtitle'] = data['Subtitle'].str.replace(r'\n', ' ', regex=True)
    data['Subtitle'] = data['Subtitle'].str.strip()

    data['Content'] = data['Content'].str.encode("ascii", "ignore").str.decode('ascii')
    data['Content'] = data['Content'].str.replace(r'\n', ' ', regex=True)
    data['Content'] = data['Content'].str.strip()
