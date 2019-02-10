from InstagramAPI import InstagramAPI
import numpy as np
import random
import time
import pickle
import os



def getTotalFollowers(api, user_id, self_following_pk):
    followers = []
    next_max_id = True
    while next_max_id:
        # first iteration hack
        if next_max_id is True:
            next_max_id = ''

        _ = api.getUserFollowers(user_id, maxid=next_max_id)
        followers.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')

        for follower in followers:

            if follower['pk'] in self_following_pk:
                continue
            if follower['pk'] in get_white_list():
                continue
            if follower['pk'] in get_black_list():
                continue

            _ = api.getUsernameInfo(follower['pk'])
            username = api.LastJson['user']['username']

            if is_bot(api, self_following_pk):
                print(username, "is bot")
                # api.block(follower['pk'])
                add_to_blacklist(follower['pk'])
                print("Append to BlackList:", username)
            else:
                print(username, "is not bot")
                # WhileList.append(follower['pk'])
                # with open(WhiteListPath, 'wb') as f:
                #     pickle.dump(WhileList, f)
                add_to_whitelist(follower['pk'])
                print("Append to WhiteList:", username)
            print("===================")
            time.sleep(random.randint(1, 3))
    return followers


if __name__ == "__main__":
    api = InstagramAPI("soheyl_daliraan", "Saghe Talaei va Gheime va Neshat")
    api.login()

    # user_id = '1461295173'
    user_id = api.username_id
    self_following_pk = set([x['pk'] for x in api.getTotalSelfFollowings()])
    # List of all followers
    followers = getTotalFollowers(api, user_id, self_following_pk)
    # followers = api.getTotalSelfFollowers()
    print('Number of followers:', len(followers))
