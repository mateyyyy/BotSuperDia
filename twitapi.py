import tweepy
import time

API_KEY = ""
API_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_SECRET = ""

def twitear(texto, monthly, month, day):
    client = tweepy.Client(consumer_key=API_KEY, consumer_secret=API_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_SECRET)
    print(client)
    try:
        client.create_tweet(text=texto)
    except:
        texto = 'No hubo variacion de precios y la inflacion acumulada del dia ' + str(day) + ' de ' + str(month) + ' es del: ' + str(monthly) + '%'
        client.create_tweet(text=texto)


def twitearRateIndividual(texto):
    client = tweepy.Client(consumer_key=API_KEY, consumer_secret=API_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_SECRET)
    print(client)
    try:
        client.create_tweet(text=texto)
    except:
        print('No pudo twitear')