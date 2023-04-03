import pandas as pd
import plotly.graph_objects as go

# Load the Excel file into a pandas DataFrame
df = pd.read_excel('snscrape1.xlsx')

# Convert the 'Date' column to a datetime object
df['Date'] = pd.to_datetime(df['Date'])

# Extract the hour from the 'Date' column and create a new column called 'Hour'
df['Hour'] = df['Date'].dt.hour

# Group the DataFrame by 'Hour' and count the number of tweets per hour
hour_tweet_counts = df.groupby('Hour')['Tweet'].count().reset_index(name='Tweet_Count')

# Create a heatmap using Plotly
fig = go.Figure(data=go.Heatmap(
                   x=hour_tweet_counts['Hour'],
                   y=[0],
                   z=[hour_tweet_counts['Tweet_Count']],
                   colorscale='Reds'))

# Set the axis titles and adjust the layout
fig.update_layout(title='Tweets per Hour', xaxis_title='Hour', yaxis_title='')

# Show the plot
fig.show()
