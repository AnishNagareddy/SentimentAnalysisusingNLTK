# SentimentAnalysisusingNLTK
* Sentiment Analysis of Aljazeera Articles using NLP Machine Learning Models 
* The total time of operation to run this code was around 15 seconds on average

## Getting Started

### Installing all the packages 
```
pip install -r requirements.txt
```
### Executing the program
```
<python main.py>
```
## Overview of the Project 

### Web Parsing 
* Used Beautiful Soup to parse through the cover page at https://www.aljazeera.com/where/mozambique/ and collected all the URLs of the relevant news articles in the page 
* With the URL, I parsed through each HTML and took the Title, Description, Data, and Content of each article and exported them to a JSON file 
## Sentiment Analysis using NLTK 
* Used NLTK's Valence Aware Dictionary and sEntiment Reasone (VADER) model to predict the positive or negative sentiment of each article and I outputted that into a CSV file
### Plotly Visualizations 
#### Barplot
![Barplot](/Plots/bar.png)
#### Scatterplot
![Scatterplot](/Plots/scatterplot.png)
## Extra 
* I also made another parser that takes the article and stores sentence by sentence for more data points in model training. 
* This is not used in the main script but could be helpful for the future 
* Also used the tqdm library to show real time processing of the program on the command line interface
## Help

* If you run into any issues or have any further ideas for this project, please contact me at nagaredd@usc.edu!

