# Stewie

A minimal, extendable bot for Mattermost written in Python and inspired by Slack's Stuart.

### Installation

The easiest way to install is using docker. You will need to create and mount 
a `config.py` file for which an example template is in the `stewie` directory.

```bash
$ git clone https://github.com/nnewman/stewie.git
$ cd stewie/stewie && cp config.template.py config.py
$ vim config.py
$ docker pull nnewman/stewie:latest
$ docker run -t -v "config.py:/opt/stewie/config.py:ro" -p "8043:8043" nnewman/stewie:latest sh -c "gunicorn -b 0.0.0.0:8043 stewie.server:app"
```

### Usage

Add a new slash command for Stewie using Mattermost. Some debugging will be necessary as you will need your team ID, which Mattermost doesn't seem to expose in the UI....

After installing, use `/stewie help` to see a list of available commands.

### Extensions

Sometimes we may want to extend Stewie without getting in the way of core functionality. Following the example
in `stewie.py`, you can write extension functions in a file within the extensions folder, and then add a config
key called `EXTENSIONS` which references your new module. Stewie will pick functions from your extensions first,
so it's possible, and encouraged, to use this mechanism to override core functionality. The hope here is that
everyone can make Stewie their own, without the need to fork him. See `extensions.py.example` for more.

### Guidelines for Contribution

I'd love to add more capabilities to Stewie, and would appreciate any feedback and/or Pull Requests which can add to him.

My requirements are, however, that any additions fit into the current design scheme and my requirements:

* All new commands must be added to the `stewie.py` file in similar format to the current scheme
* Any additional custom components should be added to the `plugins` folder for import
* Any API key settings must be added, BLANK (unless publicly available) to the `config.template.py` and imported from a config file, to be created by the user
* At the moment, no separate, non-python components will be accepted. I'm looking to add some persistent data in the future, but I'm still thinking of the best way
* Keep everything relatively clean, and work-friendly
* Productivity-friendly features will get higher priority
