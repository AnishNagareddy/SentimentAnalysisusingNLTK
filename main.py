from tqdm import tqdm
from article_parser import scrape_coverpage, article_parser, data_proccesing
from sentiment_analysis import vader_analysis, visualize_scatterplot, visualize_bar


def main():
    print("Starting Analysis:")

    coverpage_url = "https://www.aljazeera.com/where/mozambique/"
    links = []
    scrape_coverpage(coverpage_url, links)
    # remove the last element as it isnt a link
    links.pop()

    # send the links to a new function that will parse through each article
    data = article_parser(links)

    data_proccesing(data)

    # # push it to json file
    for i in tqdm(range(0, 100), desc="Converting to JSON File"):
        data.to_json('./Data/article_data.json', orient="index", indent=4)

    for i in tqdm(range(0, 100), desc="Performing VADER Analysis and Converting Data to CSV"):
        vader_analysis(data)
        data.to_csv('./Data/Article_Final_Data.csv')

    for i in tqdm(range(0, 1), desc="Saving Visualization Plots"):
        visualize_bar(data, "bar.png")
        visualize_scatterplot(data, 'scatterplot.png')

    print("Analysis Finished!")


if __name__ == '__main__':
    main()
