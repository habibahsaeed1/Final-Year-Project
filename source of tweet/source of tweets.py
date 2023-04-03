import pandas as pd
import plotly.express as px

# Load the Excel file into a pandas dataframe
df = pd.read_excel('snscrape1.xlsx')

# Use pandas to group the tweets by source
df_grouped = df.groupby('source').count().reset_index()

# Use plotly to create an interactive pie chart
fig = px.pie(df_grouped, values='Tweet', names='source')

# Show the chart
fig.show()