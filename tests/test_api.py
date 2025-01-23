from dotenv import dotenv_values
env_vars = dotenv_values(".env") 

config = dict(
url = env_vars["URL"],
team_name = env_vars["TEAM_NAME"],
token = env_vars["TOKEN"],
)

test_channel_name = env_vars["TEST_CHANNEL_NAME"]
test_user_name = env_vars["TEST_USER_NAME"]

def test_notify_channel():
    from mattermost_notify.api import notify_channel, wakeup_notify
    wakeup_notify(config=config)
    notify_channel("Hello, World!", channel_name=test_channel_name)

def test_notify_user():
    from mattermost_notify.api import notify_user, wakeup_notify
    wakeup_notify(config=config)
    notify_user("Hello, World!", user_name=test_user_name)

def test_notify_with_standard_channel():
    from mattermost_notify.api import notify_channel, wakeup_notify
    wakeup_notify(config=config, always_send_to_channel=test_channel_name)
    notify_channel("Hello, World! once")
    notify_channel("Hello, World! twice")

def test_notify_with_standard_user():
    from mattermost_notify.api import notify_user, wakeup_notify
    wakeup_notify(config=config, always_send_to_user=test_user_name)
    notify_user("Hello, World! once")
    notify_user("Hello, World! twice")

def test_notify_with_image_upload_to_user():
    from mattermost_notify.api import notify_user, wakeup_notify
    wakeup_notify(
        config=config,
        always_send_to_user=test_user_name
    )
    notify_user("Hello, World! once", files=["tests/test_api.py", "tests/test_kitty.jpg"])
    notify_user("Hello, World! twice", files=["tests/test_api.py", "tests/test_kitty.jpg"])


def test_send_markdown_to_channel():
    from mattermost_notify.api import notify_channel, wakeup_notify
    wakeup_notify(
        config=config,
        always_send_to_channel=test_channel_name
    )
    msg = """

# This is a title

With a paragraph underneath

> then a quote here
"""
    notify_channel(msg)