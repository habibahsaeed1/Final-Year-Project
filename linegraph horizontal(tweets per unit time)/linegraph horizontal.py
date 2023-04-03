import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Read the Excel file into a Pandas DataFrame
df = pd.read_excel('snscrape1.xlsx')

# Group the data by date and count the number of tweets for each date
date_counts = df.groupby('Date').size().reset_index(name='count')

# Create a subplot with a scroll bar using Plotly
fig = make_subplots(specs=[[{"secondary_y": True}]])

# Add a scatter plot of the number of tweets by date to the subplot
fig.add_trace(go.Scatter(x=date_counts['Date'], y=date_counts['count'], name='Tweet'),
              secondary_y=False)

# Set the x-axis label and title of the subplot
fig.update_xaxes(title_text='Date and Time')

# Set the y-axis label and title of the subplot
fig.update_yaxes(title_text='Number of Tweets', secondary_y=False)

# Add a scroll bar to the subplot
fig.update_layout(xaxis=dict(rangeselector=dict(buttons=list([
    dict(count=1, label="1d", step="day", stepmode="backward"),
    dict(count=7, label="1w", step="day", stepmode="backward"),
    dict(count=1, label="1m", step="month", stepmode="backward"),
    dict(count=6, label="6m", step="month", stepmode="backward"),
    dict(step="all")
])), rangeslider=dict(visible=True), type="date"))

# Show the plot
fig.show()