import argparse
from wplay import onlinetracker
from wplay import messageblast
from wplay import messagetimer
from wplay import wchat
from wplay import savechat
from wplay import tgbot
import sys

# parse positional and optional arguments
def get_arguments():
    parser = argparse.ArgumentParser(description = 'WhatApp-play')
    parser.add_argument(
        "name",
        metavar="NAME",
        type=str,
        help="contact or group name")

    group = parser.add_mutually_exclusive_group(required = True)
    group.add_argument(
        "-wc",
        "--wchat",
        action = "store_true",
        help = "chatting from command line")

    group.add_argument(
        "-wb",
        "--wblast",
        action = "store_true",
        help = "message blast to a person")

    group.add_argument(
        "-wti",
        "--wtimer",
        action = "store_true",
        help = "send messages from time to time")

    group.add_argument(
        "-wt",
        "--wtrack",
        action = "store_true",
        help = "track online status of person")
    group.add_argument(
        "-wtb",
        "--wtgbot",
        action = "store_true",
        help = "sends tracking status to telegram bot")

    group.add_argument(
        "-pull",
        "--pull",
        action = "store_true",
        help = "save all chats")

    # group.add_argument(
    #     "-wl",
    #     "--wlocation",
    #     action = "store_true",
    #     help = "finds the location of the person")

    args = parser.parse_args()
    return args

# functions for different arguments


def match_args(args):
    if args.wtrack:
        onlinetracker.tracker(args.name)

    elif args.wtgbot:
        tgbot.telegram_message(args.name)

    elif args.wchat:
        wchat.chat(args.name)

    elif args.wblast:
        messageblast.blast(args.name)

    elif args.wtimer:
        messagetimer.msgTimer(args.name)

    elif args.pull:
        try:
            bID = int(sys.argv[3])
        except (IndexError, ValueError):
            bID = 0
        savechat.runMain('pull', str(args.name), bID)

    # elif args.wlocation:
    #     loactionfinder.finder(args.name)


def main():
    args = get_arguments()
    try:
        match_args(args)
        sys.exit(0)
    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == '__main__':
    main()
