import tweepy
import logging
import time

from util import *

class key:
    API_KEY = "XXXX"                                
    API_SECRET = "XXXX"    
    ACCESS_TOKEN = "XXXX"  
    ACCESS_TOKEN_SECRET = "XXXX"
    tweet_id = 0

def get_latest_tweet():
    k = key()
    auth = tweepy.OAuthHandler(k.API_KEY, k.API_SECRET)
    auth.set_access_token(k.ACCESS_TOKEN, k.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    username = "_LeMot_"
    your_name = "_LeMot_"
    name = '_LeMot_'
    tweet_id = fetch_comment()
    tweet_id = str(tweet_id)
    replies=[]
    all_word = print_file("list.txt")
    all_word = all_word.split("\n")
    word_list = []
    occurence_list = []
    unique_word = []
    idx = 0
    final_word = []
    for tweet in tweepy.Cursor(api.search,q='to:'+name, result_type='recent', timeout=999999).items(1000):
        try:
            idx = idx + 1
            remove_baz = tweet.text.split(" ")
            if tweet_id == tweet.in_reply_to_status_id_str:
                word_list.append(remove_baz[len(remove_baz) - 1].upper())
            for i in range(len(word_list)):
                if word_list[i] in all_word and len(word_list[i]) == 5 :
                    final_word.append(word_list[i])
            unique_word = list(dict.fromkeys(final_word))
            for i in range(len(unique_word)):
                l = unique_word[i]
                fword = final_word.count(l)
                occurence_list.append(int(fword))
            zip(*sorted(zip(occurence_list, unique_word)))
            
        except:
            print("aucun")
            return("aucun")
    try:
        print(unique_word)   
        print(unique_word[0].upper())    
        return(unique_word[0].upper())
    except:
        print("aucun")
        return("aucun")        
        
def make_tweet(msg):
    k = key()
    auth = tweepy.OAuthHandler(k.API_KEY, k.API_SECRET)
    auth.set_access_token(k.ACCESS_TOKEN, k.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    username = "_LeMot_"
    your_name = "_LeMot_"
    try:
        api.update_status(msg)
    except:
        print(msg)
        print("duplicate tweet")
    
def fetch_comment():
    k = key()
    auth = tweepy.OAuthHandler(k.API_KEY, k.API_SECRET)
    auth.set_access_token(k.ACCESS_TOKEN, k.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    username = "_LeMot_"
    your_name = "_LeMot_"
    tweets = api.user_timeline(screen_name=username,count=200,include_rts = False,tweet_mode = 'extended')
    all_tweets = []
    all_tweets.extend(tweets) 
    for i in range(len(all_tweets)):
        if "🤖" in all_tweets[i].full_text:
            k.tweet_id = all_tweets[i].id
            break
    return(k.tweet_id)