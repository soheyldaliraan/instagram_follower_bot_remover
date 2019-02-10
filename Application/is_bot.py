from Application.randbool import randbool
from copy import copy


def is_bot_stochastic(api_obj, self_following_pk_set):
    user_info = api_obj.LastJson['user']
    api_obj_copy = copy(api_obj)

    if not user_info['is_private']:
        _ = api_obj_copy.getUserFeed(user_info['pk'])
        for item in api_obj_copy.LastJson['items']:
            if 'caption' not in item:
                return True
            elif item['caption'] is None:
                return True
            elif len(item['caption']['text']) < 3:
                return True

    if user_info['media_count'] == 0:
        return True

    if user_info['follower_count'] >= user_info['following_count']:
        return False
    if user_info['follower_count'] > 1000:
        return False
    if user_info['pk'] in self_following_pk_set:
        return False

    prop_bot = 1 - (user_info['follower_count'] / user_info['following_count'])

    return randbool(prop_bot)


def is_bot(api_obj, self_following_pk_set):
    user_info = api_obj.LastJson['user']
    api_obj_copy = copy(api_obj)

    if not user_info['is_private']:
        _ = api_obj_copy.getUserFeed(user_info['pk'])
        for item in api_obj_copy.LastJson['items']:
            if 'caption' not in item:
                return True
            elif item['caption'] is None:
                return True
            elif len(item['caption']['text']) < 3:
                return True

    if user_info['media_count'] == 0:
        return True

    if user_info['follower_count'] >= user_info['following_count']:
        return False
    if user_info['follower_count'] > 1000:
        return False
    if user_info['pk'] in self_following_pk_set:
        return False

    return True
