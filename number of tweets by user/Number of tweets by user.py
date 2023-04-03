import pandas as pd
import plotly.express as px

# Read the Excel file into a Pandas DataFrame
df = pd.read_excel('snscrape1.xlsx')

# Group the data by user and count the number of tweets for each user
user_counts = df.groupby('User').size().reset_index(name='count')

# Create an interactive scatter plot using Plotly
fig = px.scatter(user_counts, x='count', y='User', size='count', color='count',
                 hover_name='User', title='Number of Tweets by User')
fig.update_xaxes(title_text='Number of Tweets')
fig.update_yaxes(title_text='User')
fig.show()