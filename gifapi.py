import requests
import json
from random import randint

def gif_request(key_word):
    api_key = 'RCSVGQVJQFBB'
    gifs = requests.get("https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (key_word, api_key, 15))

    if gifs.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        giffying = json.loads(gifs.content)
        outfile = open('gif.json', 'w')
        json.dump(giffying, outfile)
        return giffying["results"][randint(0,14)]['media'][0]['mediumgif']['url']
    



import pywhatkit

def whatsapp(number, gif):

    pywhatkit.sendwhatmsg('+19198008684','https://media.giphy.com/media/1hqYk0leUMddBBkAM7/giphy.gif', 20, 6, 32)

