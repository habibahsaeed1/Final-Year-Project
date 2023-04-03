import pandas as pd
import cufflinks as cf
import plotly.express as px

# Load the Excel file into a pandas dataframe
df = pd.read_excel('snscrape1.xlsx')

# Convert the 'Time' column to a datetime object and extract the hour
df['Hour'] = pd.to_datetime(df['Date']).dt.hour

# Pivot the dataframe to create a heatmap
heatmap_data = df.pivot_table(index='Hour', values=['Likes', 'Replies', 'Retweet'], aggfunc='sum')

# Create the interactive heatmap using Plotly and Cufflinks
heatmap_fig = heatmap_data.iplot(kind='heatmap', colorscale='blues', asFigure=True)

# Set the plot title and axis labels
heatmap_fig.update_layout(title='Engagement by Time of Day', xaxis_title='Engagement Type', yaxis_title='Hour of Day')

# Show the plot
heatmap_fig.show()