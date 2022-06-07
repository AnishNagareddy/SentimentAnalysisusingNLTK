import plotly.express as px
from nltk.sentiment import SentimentIntensityAnalyzer


# using VADER form the nltk library in order to calculate compound values and then seperate each sentence

def vader_analysis(df):
    sia = SentimentIntensityAnalyzer()
    polarity_score = []
    pos = []
    neg = []
    neu = []
    label = []
    for sentence in df['Content']:
        score = sia.polarity_scores(sentence)
        # print(score)
        polarity_score.append(score['compound'])
        pos.append(score['pos'])
        neg.append(score['neg'])
        neu.append(score['neu'])
        if score['compound'] < 0.0:
            label.append('Negative')
        elif score['compound'] == 0.0:
            label.append('Neutral')
        elif score['compound'] > 0.0:
            label.append('Positive')
    df['Positive'] = pos
    df['Negative'] = neg
    df['Neutral'] = neu
    df['Polarity Score'] = polarity_score
    df['Label'] = label


def visualize_bar(df, name):
    plt = px.bar(df, x='Label')
    # plt.show()
    plt.write_image('Plots/' + name, engine="kaleido")


def visualize_scatterplot(df, name):
    plt = px.scatter_3d(df, x='Positive', y='Negative', z='Neutral', color='Label')
    # plt.show()
    plt.write_image('Plots/' + name, engine="kaleido")
