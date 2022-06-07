import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm


def scrape_coverpage(coverpage_url, links=[]):
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


def article_parser(links=[]):
    df = pd.DataFrame(columns=['Content'])
    content = []

    for link in tqdm(links, desc="Parsing Articles"):
        r = requests.get(link)
        article_page = r.content
        soup = BeautifulSoup(article_page, 'html.parser')
        content.append(str(soup.find('h1').get_text()))
        content.append(str(soup.find('em').get_text()))
        article_content = str(soup.find('div', {'class': 'wysiwyg wysiwyg--all-content css-1ck9wyi'}).get_text())
        article_c_arr = article_content.split('\n')
        for i in article_c_arr:
            content.append(i)
    df['Content'] = content
    df = df.drop(df[df['Content'] == ""].index | df[df['Content'] == " "].index)
    return df


if __name__ == '__main__':
    coverpage_url = "https://www.aljazeera.com/where/mozambique/"
    links = []
    scrape_coverpage(coverpage_url, links)
    # remove the last element as it isnt a link
    links.pop()

    df = article_parser(links)

    for i in tqdm(range(0, 100), desc="Converting to JSON File"):
        jsn = df.to_json('./Data/sentence_data.json', orient="index", indent=4)


