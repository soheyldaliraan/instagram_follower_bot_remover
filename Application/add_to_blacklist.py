import configuration
from Application.get_blacklist import get_blacklist


def add_to_blacklist(pk, username):
    black_list = get_blacklist()

    with open(configuration.blacklist_path, 'a+') as f:
        black_list.append(pk)
        f.writelines("\n" + str(pk )+ "," + str(username))
