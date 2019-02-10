import time
import random
from InstagramAPI import InstagramAPI

import configuration

from Application.get_blacklist import get_blacklist
from Application.add_to_blacklist import add_to_blacklist

from Application.get_whitelist import get_whitelist
from Application.add_to_whitelist import add_to_whitelist

from Application.is_bot import is_bot_stochastic


def find_and_block(api, user_id, self_following_pk):
    followers = []
    next_max_id = True
    while next_max_id:

        if next_max_id is True:
            next_max_id = ''

        _ = api.getUserFollowers(user_id, maxid=next_max_id)
        followers.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')

        for follower in followers:

            if follower['pk'] in self_following_pk:
                continue
            if follower['pk'] in get_whitelist():
                continue
            if follower['pk'] in get_blacklist():
                continue

            _ = api.getUsernameInfo(follower['pk'])
            username = api.LastJson['user']['username']

            if is_bot_stochastic(api, self_following_pk):
                print(username, "is bot")
                add_to_blacklist(follower['pk'], username)
                print("Append to BlackList:", username)
                api.block(follower['pk'])
                print("Blocked:", username)
            else:
                add_to_whitelist(follower['pk'], username)
                print("Append to WhiteList:", username)
            print("===================")
            time.sleep(random.randint(1, 3))
    return followers


if __name__ == "__main__":
    api = InstagramAPI(configuration.username, configuration.password)
    api.login()

    user_id = api.username_id
    self_following_pk = set([user['pk'] for user in api.getTotalSelfFollowings()])

    find_and_block(api, user_id, self_following_pk)
