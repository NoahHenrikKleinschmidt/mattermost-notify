.. mattermost-notify documentation master file, created by
   sphinx-quickstart on Thu Jan 23 13:11:20 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


Use the Command Line Interface
==============================

The Mattermost Notify package comes with a command line interface (CLI) that allows you to send messages to your Mattermost server.

The primary command is `send` which allows you to send messages to channels or users. The command has the following syntax:

.. code:: bash

   mattermost-notify send "your message" --channel <channel_name> OR --user <user_name>

The command requires that your message is enclosed in quotes. You can send messages to channels or users by providing the `--channel` or `--user` flag respectively (they are mutually exclusive, so you can only send either to a channel or to a user at one time).

You can also upload files alongside your message by providing the `--files` option, followed by a list of file paths separated by spaces. The files will be uploaded to the Mattermost server and linked in the message.
For example:

.. code:: bash

   now=$(date +"%Y-%m-%d %H:%M:%S")
   mattermost-notify send "Logfile from: $now" --channel simulations --files /path/to/simulations/logfile.txt

The command will send the message to the `simulations` channel and upload the file `logfile.txt` to the channel.


Specifying a Configuration File
-------------------------------

Mattermost Notify stores the connection data and login credentials in a configuration file (which is automatically generated if you ran `mattermost-notify setup`). The configuration file is located in the user's home directory and is named `.mattermost-notify`.
If for some reason you want to use a different configuration file (e.g. to send to a different server), you can specify it using the `--configfile` option. For example:

.. code:: bash

   mattermost-notify send "this is a test" --channel simulations --configfile /path/to/your/.mattermost-notify


