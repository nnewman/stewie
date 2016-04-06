# Stewie

_**VERY ALPHA**_

A minimal bot for Mattermost written in Python and inspired by Slack's Stuart.

Usage:

Add a new slash command for Stewie using Mattermost. Some debugging will be necessary as you will need your team ID, which Mattermost doesn't seem to expose in the UI....

After installing, use `/stewie help` to see a list of available commands.

### Guidelines for Contribution

I'd love to add more capabilities to Stewie, and would appreciate any feedback and/or Pull Requests which can add to him.

My requirements are, however, that any additions fit into the current design scheme and my requirements:

* All new commands must be added to the `stewie.py` file in similar format to the current scheme
* Any additional custom components should be added to the `plugins` folder for import
* Any API key settings must be added, BLANK (unless publicly available) to the `config.template.py` and imported from a config file, to be created by the user
* At the moment, no separate, non-python components will be accepted. I'm looking to add some persistent data in the future, but I'm still thinking of the best way
* Keep everything relatively clean, and work-friendly
* Productivity-friendly features will get higher priority
