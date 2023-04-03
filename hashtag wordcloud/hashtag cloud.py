import pandas as pd
import re
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud, STOPWORDS
from bidi.algorithm import get_display
import arabic_reshaper

# Read the excel file
df = pd.read_excel('hashtagcloud tweets.xlsx')

# Define function to extract hashtags from each tweet
def extract_hashtags(text):
    hashtags = re.findall(r'\#\w+', text)
    return hashtags

# Create a list of all hashtags in the dataframe
all_hashtags = []
for tweet in df['tweet']:
    hashtags = extract_hashtags(tweet)
    all_hashtags.extend(hashtags)

# Create a dictionary to store the frequency of each hashtag
frequency = {}
for hashtag in all_hashtags:
    if hashtag in frequency:
        frequency[hashtag] += 1
    else:
        frequency[hashtag] = 1

# Write the hashtag frequency to a text file
with open('hashtag_frequency.txt', 'w', encoding='utf-8') as f:
    for hashtag in frequency:
        f.write('{}\t{}\n'.format(hashtag, frequency[hashtag]))


# Generate a word cloud of the hashtags
wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                min_font_size = 10,
                font_path = 'AwamiNastaliq-Regular.ttf',
                collocations=False,
                prefer_horizontal=0.9).generate_from_frequencies(frequency)

# Reshape the Urdu text to display it correctly in the wordcloud
#reshaped_text = arabic_reshaper.reshape(wordcloud.words_)
#display_text = get_display(reshaped_text)

# Plot the WordCloud image
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)

# Display the WordCloud image
plt.show()