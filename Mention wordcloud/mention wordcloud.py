import pandas as pd
import re
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud, STOPWORDS

# Read the excel file
df = pd.read_excel('snscrape1.xlsx')

# Define function to extract hashtags from each tweet
def extract_mentions(text):
    mentions = re.findall(r'\@\w+', text)
    return mentions

# Create a list of all hashtags in the dataframe
all_mentions = []
for tweet in df['Tweet']:
    mentions = extract_mentions(tweet)
    all_mentions.extend(mentions)

# Create a dictionary to store the frequency of each hashtag
frequency = {}
for mentions in all_mentions:
    if mentions in frequency:
        frequency[mentions] += 1
    else:
        frequency[mentions] = 1

# Write the hashtag frequency to a text file
with open('hashtag_frequency.txt', 'w', encoding='utf-8') as f:
    for mentions in frequency:
        f.write('{}\t{}\n'.format(mentions, frequency[mentions]))


# Generate a word cloud of the hashtags
wordcloud = WordCloud(width = 1300, height = 800,
                background_color ='black',
                min_font_size = 8,
                max_words=200,
                font_path = 'AwamiNastaliq-Regular.ttf',
                collocations=False,
                prefer_horizontal=0.9).generate_from_frequencies(frequency)


# Plot the WordCloud image
plt.figure(figsize = (10, 10), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)

# Display the WordCloud image
plt.show()