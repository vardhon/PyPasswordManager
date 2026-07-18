import json
def load_passwords():
    try:
        with open("data/pass.json") as data:
            return json.load(data)
    except FileNotFoundError:
        return {}

def save_password(dict_data):
    with open("data/pass.json", mode="w") as data:
        json.dump(dict_data, data, indent=4)

def search_password(search_site):
    return load_passwords().get(search_site)


def update_password():
    pass