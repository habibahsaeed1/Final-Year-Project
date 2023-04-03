import pandas as pd
import plotly.graph_objs as go

# Read the Excel file into a Pandas DataFrame
df = pd.read_excel('snscrape1.xlsx')

# Find the tweet with the highest number of likes, replies, and retweets for each user
max_likes = df.groupby('User')['Likes'].max()
max_replies = df.groupby('User')['Replies'].max()
max_retweets = df.groupby('User')['Retweet'].max()

# Find the user with the tweet with the highest number of likes, replies, and retweets
max_likes_user = max_likes.idxmax()
max_replies_user = max_replies.idxmax()
max_retweets_user = max_retweets.idxmax()

# Create a bar chart of the number of likes, replies, and retweets for each user
fig = go.Figure(data=[
    go.Bar(name='Likes', x=max_likes.index, y=max_likes),
    go.Bar(name='Replies', x=max_replies.index, y=max_replies),
    go.Bar(name='Retweets', x=max_retweets.index, y=max_retweets)
])

# Add annotations for the user with the tweet with the highest number of likes, replies, and retweets
fig.update_layout(
    barmode='group',
    title='User Engagement Metrics',
    xaxis_title='User',
    yaxis_title='Count',
    annotations=[
        dict(x=max_likes_user, y=max_likes[max_likes_user],
             xref="x", yref="y", text="Max Likes", showarrow=True, arrowhead=1, ax=-30, ay=-40),
        dict(x=max_replies_user, y=max_replies[max_replies_user],
             xref="x", yref="y", text="Max Replies", showarrow=True, arrowhead=1, ax=-30, ay=-40),
        dict(x=max_retweets_user, y=max_retweets[max_retweets_user],
             xref="x", yref="y", text="Max Retweets", showarrow=True, arrowhead=1, ax=-30, ay=-40)
    ]
)

# Show the plot
fig.show()