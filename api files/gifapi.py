import requests
import json
from random import randint

def gif_request(key_word):
    api_key = 'RCSVGQVJQFBB'
    gifs = requests.get("https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (key_word, api_key, 10))

    if gifs.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        giffying = json.loads(gifs.content)
        outfile = open('gif.json', 'w')
        json.dump(giffying, outfile)
        return giffying["results"][randint(0,10)]['media'][0]['mediumgif']['url']
    


print(gif_request('cute'))