import pandas as pd
import plotly.graph_objs as go
import matplotlib.pyplot as plt

# Load the Excel file into a pandas dataframe
df = pd.read_excel('snscrape1.xlsx')

# Convert the 'Date' column to a pandas datetime object
df['Date'] = pd.to_datetime(df['Date'])

# Set the 'Date' column as the index of the dataframe
df.set_index('Date', inplace=True)

# Create traces for each engagement type
retweets_trace = go.Scatter(x=df.index, y=df['Retweet'], name='Retweets')
likes_trace = go.Scatter(x=df.index, y=df['Likes'], name='Likes')
replies_trace = go.Scatter(x=df.index, y=df['Replies'], name='Replies')

# Create a list of traces
data = [retweets_trace, likes_trace, replies_trace]

# Create the layout for the plot
layout = go.Layout(title='Twitter Engagement Over Time',
                   xaxis=dict(title='Date'),
                   yaxis=dict(title='Number of Engagements'))

# Create the figure object and plot it
fig = go.Figure(data=data, layout=layout)
fig.show()