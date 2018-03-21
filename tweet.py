import tweepy
 
def login_to_twitter(consumer_key, consumer_secret, access_token, access_token_secret):
 
    auth = tweepy.OAuthHandler(consumer_key,  consumer_secret)
    auth.set_access_token(access_token,       access_token_secret)
 
    api = tweepy.API(auth)
    ret = {}
    ret['api'] = api
    ret['auth'] = auth
    return  api
 
 
 
def post_tweets():
 
    consumer_key	   =   'MnQ43dUYm3pdLBfo7CwSn5D62'
    consumer_secret	   =   'QGDolutNu2XOilPkUAYdrFQ84YEX9BbdC8o6mRrCFzsX7ujUzO'
    access_token	   =   '20350047-SyLZ29K3HRIeIfTtpLpVbapSqQwFtWXHdIQWNf3Tw'
    access_token_secret=   'fndMycPtFEBZ08j6Y4mXwvkVJtg5JVHZuqYZVodpwn2fn'
 
    message = "Hello,\nHow are you doing today"
 
    api = login_to_twitter(consumer_key, consumer_secret, access_token, access_token_secret )
 
    ret = api.update_status(status=message)
 
 
if __name__ == '__main__':
    post_tweets()