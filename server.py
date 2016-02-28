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
                          "someone! The error was {}".format(e))

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
        if text == '':
            command, args = 'help', text
        else:
            command, args = command_processor(text)
        if getattr(Stewie, command):
            baby_talk = getattr(Stewie, command)(args)
        response = slack.response(baby_talk, response_type=shared(text))
        return response
    except Exception(e):
        return exception_alert(e)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=True)
