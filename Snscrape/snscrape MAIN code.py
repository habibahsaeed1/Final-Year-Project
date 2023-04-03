import snscrape.modules.twitter as sntwitter
import pandas as pd
from datetime import datetime

query="(#imrankhan) -filter:replies"
tweets = []
limit = 500

for tweet in sntwitter.TwitterHashtagScraper(query).get_items():
    # print(vars(tweet))
    # break
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.id, tweet.date, tweet.user.username, tweet.content, tweet.likeCount, tweet.replyCount,
                       tweet.retweetCount, tweet.lang, tweet.url, tweet.hashtags, tweet.coordinates, tweet.place,
                       tweet.retweetedTweet, tweet.source,tweet.mentionedUsers])

df = pd.DataFrame(tweets, columns=['ID', 'Date', 'User', 'Tweet', 'Likes', 'Replies', 'Retweet', 'Language', 'URL', 'Hashtags',
                           'coordinates', 'place', 'retweetedTweet', 'source','mentions'])

# to save to excel file
df['Date'] = pd.to_datetime(df['Date'],unit='ms')
df['Date'] = df['Date'].apply(lambda a: datetime.strftime(a,"%Y-%m-%d %H:%M:%S"))
df['Date'] = pd.to_datetime(df['Date'])
df.to_excel('scrappedtweets.xlsx',index=False, engine='xlsxwriter')