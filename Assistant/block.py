from InstagramAPI import InstagramAPI
from Application.get_blacklist import get_blacklist
import configuration
import time
from random import randint
from Application.remove_from_blacklist import remove_from_blacklist

if __name__ == "__main__":
    api = InstagramAPI(configuration.username, configuration.password)
    api.login()

    blacklist = get_blacklist()

    for pk in blacklist:
        api.block(int(pk))
        print("Blocked:", pk)

        remove_from_blacklist(pk)
        time.sleep(randint(1, 3))
