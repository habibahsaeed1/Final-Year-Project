# Import necessary libraries
import pandas as pd
import plotly.graph_objects as go
from textblob import TextBlob
from collections import defaultdict

# Load the data from Excel file
df = pd.read_excel('snscrape1.xlsx')


# Define function to calculate sentiment polarity
def get_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity


# Create a dictionary to store sentiment values for each user
sentiments = defaultdict(list)

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    # Get the user and tweet
    user = row['User']
    tweet = row['Tweet']

    # Calculate sentiment polarity of the tweet
    sentiment = get_sentiment(tweet)

    # Append sentiment to the list of sentiments for the user
    sentiments[user].append(sentiment)

# Create a list of traces for each user
traces = []
for user in df['User'].unique():
    user_sentiments = sentiments[user]
    indices = list(range(1, len(user_sentiments) + 1))
    trace = go.Scatter(x=indices, y=user_sentiments, mode='markers+lines', name=user)
    traces.append(trace)

# Create the plot with all traces
fig = go.Figure(data=traces)
fig.update_layout(title="Sentiment Analysis for Users",
                  xaxis_title='Tweets',
                  yaxis_title='Sentiment Polarity')
fig.show()
