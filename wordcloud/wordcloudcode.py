import pandas as pd
import re
import nltk
from collections import Counter
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load the Excel file containing the tweets
tweets_df = pd.read_excel('hashtagcloud tweets.xlsx')

# Define the function to clean the text data
def clean_text(text):
    # Remove hashtags and symbols
    text = re.sub(r'#\w+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    # Remove emojis
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)
    text = emoji_pattern.sub(r'', text)
    # Convert to lowercase
    text = text.lower()
    # Tokenize the text
    tokens = nltk.word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    stop_words_urdu = set(stopwords.words('urdu'))
    tokens = [token for token in tokens if not token in stop_words and not token in stop_words_urdu]
    # Join the tokens back into a string
    text = ' '.join(tokens)
    return text

# Clean the text data
tweets_df['cleaned_text'] = tweets_df['tweet'].apply(clean_text)

# Count the frequency of keywords in the cleaned text
keywords = []
for text in tweets_df['cleaned_text']:
    keywords.extend(text.split())
keyword_freq = dict(Counter(keywords))

# Write the keyword frequency data to a text file
with open('keyword_freq.txt', 'w', encoding='utf-8') as file:
    for keyword, freq in keyword_freq.items():
        file.write(f'{keyword}: {freq}\n')

# Generate a word cloud
wordcloud = WordCloud(width=800, height=800, background_color='white',font_path = 'AwamiNastaliq-Regular.ttf', max_words=200).generate_from_frequencies(keyword_freq)
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()