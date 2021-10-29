from social import Twitter
from account_args import account_info 
from accounts import creds
tweet = Twitter(account_info())
#tweet.tweet_text_only('Here is another tweet generated from a python script')
img = tweet.twitter_media_upload('TWO.png')
id = img.media_id
tweet.tweet_text_and_media('NHC Tropical Weather Outlokk', id)
