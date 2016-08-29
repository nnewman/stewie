import os
import sys
import requests

import urbandict
from plugins import yelp

import config

def command_processor(text):
    words = text.split(' ')
    if words[0] == '!':
        words = words[1:]
    return words[0], words[1:]

class Stewie(object):

    @staticmethod
    def joke(*args):
        response = requests.get(config.JOKE_URL)
        return response.json()['joke']

    @staticmethod
    def food(*args):
        yelp_search = yelp.search(' '.join(args[0]), config.HOME_LOCATION)
        results = yelp_search['businesses'][0]
        return "How about [{0}]({1})?".format(results['name'],
                                              results['url'])

    @staticmethod
    def define(*args):
        definition = urbandict.define(' '.join(args[0]))[0]
        return "### {} \n **Definition**: {} \n **Example**: _{}_".format(
                definition['word'],
                definition['def'],
                definition['example']
        )

    @staticmethod
    def gif(*args):
        payload = {
            's': ' '.join(args[0]),
            'api_key': config.GIPHY_KEY
        }
        response = requests.get(config.GIPHY_ENDPOINT + '/translate',
                                params=payload)
        response = response.json()['data']
        if response['rating'] not in ['y', 'g', 'pg', 'pg-13']:
            return "### Uh oh... \n I don't think Lois would want me " \
                   "to see this."
        else:
            return "![]({})".format(response['images']['fixed_height']['url'])

    @staticmethod
    def butts(*args):
        payload = {
            'ids': 'OCu7zWojqFA1W',
            'api_key': config.GIPHY_KEY
        }
        response = requests.get(config.GIPHY_ENDPOINT, params=payload)
        response = response.json()['data'][0]
        return "![]({})".format(response['images']['fixed_height']['url'])

    @staticmethod
    def help(*args):
        help_text = """
# ![](https://s3.amazonaws.com/mm-resources-01/stewie_small.png)
_Stewie_

Stewie is our bot with lots of useful and non-useful helper
functions.

"help" - Prints out this help message

---
#### Post to Channel

All commands are ephemeral by default. To post Stewie's response
to the channel use a `!` between `/stewie` and your command. Some
commands are forced to post to the channel.

#### Commands

* `help` - List of commands
* `food [query]` - Use Yelp to find a nearby eatery
* `joke` - Find a random joke
* `define [query]` - Uses UrbanDictionary to define a word
* `gif [query]` - Searches Giphy for your query
* `butts` - Hold on to your butts... deploy going up
        """
        return help_text
