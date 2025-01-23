<p align="center">
    <img src="docs/_static/mattermost-notify.png" width="15%">
</p>

# mattermost-notify
### Send notifications using a Bot account from your applications to Mattermost. Simple, fast, easy to set up. No fuzz, just works... 

[![Made with Python](https://img.shields.io/badge/Python->=3.8-blue?logo=python&logoColor=white)](https://python.org "Go to Python homepage")
[![code style - black](https://img.shields.io/badge/code_style-black-black)](https://black.readthedocs.io/ "Go to Black homepage")
![Read the Docs](https://img.shields.io/readthedocs/mattermost-notify)
![Mattermost](https://img.shields.io/badge/Mattermost-%3E=9-gray?labelColor=blue&style=flat)
![Mattermost-API](https://img.shields.io/badge/Mattermost--API-v4-gray?labelColor=blue&style=flat) 



## Installation

> First make sure to set up a Bot account on your Mattermost Server with the name `notify`. Follow the [Documentation](https://mattermost-notify.readthedocs.io/en/latest/setup_bot.html) to learn how. 


If you have your `notify`Bot account set up correctly and you have got it's access token you can install the client package using:

```bash
# (yep it's in reverse since another project already used the name on PyPi 😅)
pip install notify-mattermost
```

Then set up the connection using: 

```bash
# follow the dialog...
mattermost-notify setup
```

Now you can test your connection by sending a dummy message to your own user account by doing:

```bash
mattermost-notify send "my first message" --user your-username
```

If you set up everything correctly you should have received a message at this point!


## Quick Example from Python
The Python API is very straightforward to use. A quick example (after having set up everything at installation) would look like this:

```python
import mattermost_notify as notify

# initialze the connection
notify.wakeup()

# send a message to a channel
notify.notify("This is a test message", channel_name="some_channel")

# you can also upload files in this way
notify.notify("My latest log file", user="your_username", files=["my_pipeline/log.txt"])
``` 

