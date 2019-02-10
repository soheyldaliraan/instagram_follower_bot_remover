import configuration
from Application.get_whitelist import get_whitelist


def add_to_whitelist(pk, username):
    whitelist = get_whitelist()

    with open(configuration.whitelist_path, 'a+') as f:
        whitelist.append(pk)
        f.writelines("\n" + str(pk) + "," + str(username))
