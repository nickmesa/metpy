from social import Twitter
from account_args import account_info 
from accounts import creds
tweet = Twitter(account_info())
tweet.tweet_text_only('Here is another tweet generated from a python script')