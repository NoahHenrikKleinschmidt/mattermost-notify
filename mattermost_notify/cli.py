"""
Command line interface for Mattermost Notify
"""

from argparse import ArgumentParser

parser = ArgumentParser(description='Send messages to Mattermost with Mattermost Notify!')
command = parser.add_subparsers(dest='command', help='The command to run.')
setup = command.add_parser("setup", help="Setup the Mattermost Notify configuration.")
send = command.add_parser("send", help="Send a message to a channel or user.")
test = command.add_parser("test", help="Test the connection to the Mattermost server.")

setup.add_argument("-i", "--interactive", help="Run in interactive mode.", action="store_true")
setup.add_argument("-u", "--url", help="The URL of the Mattermost server.")
setup.add_argument("-n", "--team-name", help="The name of the team (the 'notify' bot needs to be a member!)")
setup.add_argument("-t", "--token", help="The access token for the 'notify' bot.")
setup.add_argument("-o", "--output", help="The path where to write the .mattermost_notify file. By default Mattermost Notify will search in either $PWD or $HOME (defaults to $HOME)", default="$HOME")

send.add_argument("message", help="The message to send.")
dest = send.add_argument_group("Send to", "Send the message to a channel or user.")
dest.add_argument("-c", "--channel", help="The name of the channel to send the message to. The 'notify' bot needs to have access to or be added to the channel!")
dest.add_argument("-u", "--user", help="The name of the user to send the message to.")
dest.add_argument("-f", "--files", help="The path(s) to file(s) to send as an attachment.", nargs="+", default=None)
dest.add_argument("--configfile", help="The path to a .mattermost_notify file or a directory containing such a file. By default Mattermost Notify will search in either $PWD or $HOME", default=None)

test.add_argument("--configfile", help="The path to a .mattermost_notify file or a directory containing such a file. By default Mattermost Notify will search in either $PWD or $HOME", default=None)

def main():
    args = parser.parse_args()

    if args.command == "setup":
        if args.interactive or not any([args.url, args.team_name, args.token]):
            from mattermost_notify.config import setup_config_interactive
            setup_config_interactive()
        else:
            from mattermost_notify.config import setup_config
            if args.output == "$HOME":
                args.output = None
            setup_config(args.url, args.team_name, args.token, args.output)
    
    
    elif args.command == "send":
        from mattermost_notify.client import Notify
        from mattermost_notify.config import get_config
        config = get_config(args.configfile)
        client = Notify(
            url=config["url"],
            team_name=config["team_name"],
            token=config["token"]
        )
        if args.channel:
            client.send_to_channel(args.message, channel_name=args.channel, files=args.files)
        elif args.user:
            client.send_to_user(args.message, user_name=args.user, files=args.files)
    
    
    elif args.command == "test":
        from mattermost_notify.client import Notify
        from mattermost_notify.config import get_config
        config = get_config(args.configfile)
        client = Notify(
            url=config["url"],
            team_name=config["team_name"],
            token=config["token"]
        )
        assert client.test_connection(), "Connection failed"
        print("Connection successful!")
    
    else:
        parser.print_help()

if __name__ == "__main__":

    main()