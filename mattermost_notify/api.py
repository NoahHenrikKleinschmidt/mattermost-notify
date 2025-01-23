
from .client import Notify
from .config import get_config

__notify = None
"""
The default notify client
"""

__default_user = None
"""
The default user to send messages to
"""

__default_channel = None
"""
The default channel to send messages to
"""

def wakeup_notify(always_send_to_user: str = None, always_send_to_channel: str = None, config: dict = None) -> Notify:
    """
    Create a Notify client

    Parameters
    ----------
    always_send_to_user : str
        The default user to send messages to
    always_send_to_channel : str
        The default channel to send messages to
    config : dict
        The configuration to use. By default a configuration file will be searched for. The dictionary must contain keys: "url", "team_name", and "token".
    """
    global __notify
    if config is None:
        config = get_config()
    client = Notify(
        url=config["url"],
        team_name=config["team_name"],
        token=config["token"]
    )
    __notify = client
    if always_send_to_user and always_send_to_channel:
        raise ValueError("Default settings are mutually exclusive! Cannot send to both a user and a channel")
    if always_send_to_user:
        global __default_user
        __default_user = always_send_to_user
    if always_send_to_channel:
        global __default_channel
        __default_channel = always_send_to_channel
    return client

def notify_channel(message: str, channel_name: str=None, files: list = None):
    """
    Send a message to a channel

    Parameters
    ----------
    message : str
        The message to send
    channel_name : str
        The name of the channel to send the message to
    files: list
        A list of file paths of files to upload  to the channel
    """
    if __notify is None:
        wakeup_notify()
    if channel_name is None and __default_channel is None:
        raise ValueError("No channel specified and no default channel set")
    if channel_name is None:
        channel_name = __default_channel
    __notify.send_to_channel(message, channel_name=channel_name, files=files)

def notify_user(message: str, user_name: str = None, files: list = None):
    """
    Send a message to a user

    Parameters
    ----------
    message : str
        The message to send
    user_name : str
        The name of the user to send the message to
    files: list
        A list of file paths of files to upload  to the user-chat
    """
    if __notify is None:
        wakeup_notify()
    if user_name is None and __default_user is None:
        raise ValueError("No user specified and no default user set")
    if user_name is None:
        user_name = __default_user
    __notify.send_to_user(message, user_name=user_name, files=files)

__all__ = ["wakeup_notify", "notify_channel", "notify_user"]