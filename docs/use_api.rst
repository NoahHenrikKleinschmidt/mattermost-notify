.. mattermost-notify documentation master file, created by
   sphinx-quickstart on Thu Jan 23 13:11:20 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


Use the Python API
==================

The Mattermost Notify package comes with a Python API that allows you to send messages to your Mattermost server.

Functional API
--------------

There are a handful of toplevel functions that allow you to send messages without much fuzz.
The first function to call is `wakeup()` which will initialize a connection automatically, assuming you have properly
`set up Mattermost Notify`_ after installing the package.

.. _set up Mattermost Notify: setup_package

After that you can use the functions `notify_user` and `notify_channel` to send messages and files to users or channels respectively.
You can also use the `notify` function to do either of these things, but you will have to specify the target every time.

Here is a small toy example:

.. code:: python

   import mattermost_notify as notify

   # initialize the connection
   notify.wakeup()

   # send a message to a user
   notify.notify_user("Hello World!", "your_username") 

   # send a message and a file to a channel
   notify.notify_channel("Hello World!", "channel_name", files=["/path/to/file"])


The `Notify` class
------------------

The primary class is the `Notify` class that you can use to set up a connection to your Mattermost server and send messages.
If you prefer having a class object rather than using the toplevel functions, you can use the `Notify` class, which you will have to set up manually.

Here is an example:

.. code:: python

   import mattermost_notify as notify

   # create a Notify object
   client = notify.Notify(token="your_token", url="your_server_url", team_name="your_team_name")

   # send a message to a user
   client.send_to_user("Hello World!", "your_username")


The `Notify` class also has a `send_to_channel` method that allows you to send messages to channels.

.. code:: python

   # send a message to a channel
   client.send_to_channel("Hello World!", "channel_name")


If you want to upload files alongside your message, you can provide a list of file paths to either of these functions using the `files` argument.

.. code:: python

   # send a message to a channel with two files
   client.send_to_channel("Hello World!", "channel_name", files=["/path/to/file1", "/path/to/file2"])


Standard User or Channel
------------------------

The functional API supports setting a standard target for messages so that the user does not have to repeat the target in every call.
The `Notify` class supports this feature only for channels.

Here is an example:

.. code:: python

   import mattermost_notify as notify

   # set up and specify that by default messages should go to a specific user
   notify.wakeup(always_send_to_user="your_username")

   # send a message to the default user (no need to specify the target)
   notify.notify("Hello World!")



