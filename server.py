import importlib
import os

from flask import Flask, send_file
from flask_slack import Slack

import config
from stewie import Stewie, command_processor

app = Flask(__name__)
slack = Slack(app)

app.add_url_rule('/', view_func=slack.dispatch)


def exception_alert(e):
    return slack.response("### Uh oh... \n Something went wrong. Go tell "
                          "someone! The error was: {}".format(e))

def shared(text):
    if text.split(' ')[0] == '!':
        return 'in_channel'
    else:
        return 'ephemeral'

@app.route('/stewie-image')
def stewie_image():
    return send_file('stewie.jpg', mimetype='image/jpeg')

@slack.command('stewie', token=config.MATTERMOST_TOKEN,
               team_id=config.TEAM_ID, methods=['POST'])
def stewie(**kwargs):

    try:
        text = kwargs.get('text')

        if config.EXTENSIONS:
            ext = importlib.import_module(config.EXTENSIONS)
        else:
            ext = None

        if text == '':
            command, args = 'help', text
        else:
            command, args = command_processor(text)

        if ext and hasattr(ext, command):
            baby_talk = getattr(ext, command)(args, kwargs)
            if command in ext.force_noisy:
                share = 'in_channel'
            else:
                share = shared(text)

        elif hasattr(Stewie, command):
            baby_talk = getattr(Stewie, command)(args, kwargs)
            share = shared(text)

        else:
            baby_talk = "I don't know what {} means, but I'm " \
                        "just a baby...".format(command)
            share = 'ephemeral'

        response = slack.response(baby_talk, response_type=share)
        return response
    except Exception as e:
        return exception_alert(e)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=True)
