import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier

def clean_tweet(tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
 
def get_tweet_sentiment(tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        
        #try:
        cleanedTweet = clean_tweet(tweet);
        #except:
        # cleanedTweet = tweet;
        # print(tweet);
        analysis = TextBlob(cleanedTweet);
        test = analysis.sentiment.polarity;
        sentiemnt = analysis.sentiment;
        #print(test);
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

def word_in_text(word,text):
	if text == None:
		return False
	word = word.lower()
	text = text.lower() 
	match = re.search(word,text)
	if match:
		return True
	else:
		return False

tweets_data_path = 'tweets.txt.001'
fetched_tweets = []
tweets_file = open(tweets_data_path, "r")

for line in tweets_file:
    try:
        tweet = json.loads(line)
        #only india and new delhi tweets fetched
        #tweets with null locations are not included
        if tweet['user']['location'] == None or re.search('india',tweet['user']['location'].lower()) != None or re.search('new delhi',tweet['user']['location'].lower())!= None:
            if word_in_text('bjp', tweet.get('text', None)):
                fetched_tweets.append(tweet)
    except:
        continue
print (len(fetched_tweets))
tweets = pd.DataFrame()

'''
def get_tweets(self, query, count = 10):
        # empty list to store parsed tweets
        tweets = []
 
        try:
            # call twitter api to fetch tweets
            fetched_tweets = self.api.search(q = query, count = count)
 
            # parsing tweets one by one
            for tweet in fetched_tweets:
                # empty dictionary to store required params of a tweet
                parsed_tweet = {}
 
                # saving text of tweet
                parsed_tweet['text'] = tweet.text
                # saving sentiment of tweet
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)
 
                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)
 
            # return parsed tweets
            return tweets
 
        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))'''
parsed_tweets = []
for tweet in fetched_tweets:
        parsed_tweet = { };
        parsed_tweet['text'] = tweet.get('text', None)
        try:
         parsed_tweet['sentiment'] = get_tweet_sentiment(tweet.get('text', None))
        except:
         #print(tweet)
         parsed_tweet['sentiment'] = 'neutral'
         continue;
        parsed_tweets.append(parsed_tweet);
def main():
    # picking positive tweets from tweets
    ptweets = [tweet for tweet in parsed_tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    if len(ptweets) == 0 or len(fetched_tweets) == 0:
        print("Positive Tweets Not Found");
    else:            
        print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(fetched_tweets)))
    # picking negative tweets from tweets
    ntweets = [tweet for tweet in parsed_tweets if tweet['sentiment'] == 'negative']
    #print(len(tweets));
    #exit;
    # percentage of negative tweets
    if len(ntweets) == 0 or len(fetched_tweets) == 0:
        print("Negative Tweets Not Found");
    else:
        print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(fetched_tweets)))
    # percentage of neutral tweets
    print("Neutral tweets percentage: {} %".format(100* (len(fetched_tweets) - len(ntweets) - len(ptweets))/len(fetched_tweets)))
    exit; 
    # printing first 5 positive tweets
    #print("\n\nPositive tweets:")
    #for tweet in ptweets[:10]:
        #print(tweet['text'])
 
    # printing first 5 negative tweets
    #print("\n\nNegative tweets:")
    #for tweet in ntweets[:10]:
        #print(tweet['text'])
    error_tweets = 0
    '''
    for tweet in parsed_tweets:
         if tweet['sentiment'] == 'neutral' :
                   try:
                        print(tweet['text'] + "\n\n\n")
                   except:
                        error_tweets = error_tweets + 1
    #print(error_tweets);
    '''
if __name__ == "__main__":
    # calling main function
    main()

'''tweets['text'] = [ value for value in map(lambda tweet: tweet.get('text', None), tweets_data) ]
tweets['lang'] = [ value for value in map(lambda tweet: tweet.get('lang', None), tweets_data) ]
tweets['country'] = [ value for value in map(lambda tweet: tweet.get('place', {}).get('country') if tweet.get('place', None) != None else None, tweets_data) ]
tweets_by_lang = pd.value_counts(tweets['lang'])

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Languages', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')
tweets_by_country = tweets['country'].value_counts()

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Countries', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')
tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')
plt.show()'''

def word_in_text(word,text):
	if text == None:
		return False
	word = word.lower()
	text = text.lower() 
	match = re.search(word,text)
	if match:
		return True
	else:
		return False

#tweets['bjp'] = tweet.get('text', None).apply(lambda tweet: word_in_text('bjp', tweet))
#tweets['congress'] = tweets.get('text', None).apply(lambda tweet: word_in_text('congress', tweet))
#tweets['aap'] = tweets.get('text', None).apply(lambda tweet: word_in_text('aap', tweet))
#print (tweets['bjp'].value_counts()[True])
#print (tweets['javascript'].value_counts()[True])
#print (tweets['ruby'].value_counts()[True])
#prg_langs = ['bjp', 'congress', 'aap']
#tweets_by_prg_lang = [tweets['bjp'].value_counts()[True], tweets['congress'].value_counts()[True], tweets['aap'].value_counts()[True]]

#x_pos = list(range(len(prg_langs)))
#width = 0.8
#fig, ax = plt.subplots()
#plt.bar(x_pos, tweets_by_prg_lang, width, alpha=1, color='g')

# Setting axis labels and ticks
#ax.set_ylabel('Number of tweets', fontsize=15)
#ax.set_title('Ranking: bjp vs. congress vs. aap (Raw data)', fontsize=10, fontweight='bold')
#ax.set_xticks([p + 0.4 * width for p in x_pos])
#ax.set_xticklabels(prg_langs)
#plt.grid()
#plt.show()

#tweets['mcd'] = tweets.get('text', None).apply(lambda tweet: word_in_text('mcd', tweet))
#tweets['tutorial'] = tweets.get('text', None).apply(lambda tweet: word_in_text('tutorial', tweet))
#tweets['relevant'] = tweets.get('text', None).apply(lambda tweet: word_in_text('programming', tweet) or word_in_text('tutorial', tweet))
#print (tweets['mcd'].value_counts()[True])
#print (tweets['tutorial'].value_counts()[True])
#print (tweets['relevant'].value_counts()[True])
#print (tweets[tweets['relevant'] == True]['python'].value_counts()[True])
#print (tweets[tweets['relevant'] == True]['javascript'].value_counts()[True])
#print (tweets[tweets['relevant'] == True]['ruby'].value_counts()[True])
#tweets_by_prg_lang = [tweets[tweets['relevant'] == True]['python'].value_counts()[True], 
#                      tweets[tweets['relevant'] == True]['javascript'].value_counts()[True], 
#                      tweets[tweets['relevant'] == True]['ruby'].value_counts()[True]]
#x_pos = list(range(len(prg_langs)))
#width = 0.8
#fig, ax = plt.subplots()
#plt.bar(x_pos, tweets_by_prg_lang, width,alpha=1,color='g')
#ax.set_ylabel('Number of tweets', fontsize=15)
#ax.set_title('Ranking: python vs. javascript vs. ruby (Relevant data)', fontsize=10, fontweight='bold')
#ax.set_xticks([p + 0.4 * width for p in x_pos])
#ax.set_xticklabels(prg_langs)
#plt.grid()
#plt.show()