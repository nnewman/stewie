import requests

from plugins import yelp
import urbandict

import config

def command_processor(text):
    words = text.split(' ')
    if words[0] == '!':
        words = words[1:]
    return words[0], words[1:]

class Stewie(object):

    @staticmethod
    def help(*args):
        with open('stewie.md') as f:
            return f.read()

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
    def cramit(*args):
        payload = {
            'ids': 'xTiTnz3X5xhG9ybqJa',
            'api_key': config.GIPHY_KEY
        }
        response = requests.get(config.GIPHY_ENDPOINT, params=payload)
        response = response.json()['data'][0]
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
