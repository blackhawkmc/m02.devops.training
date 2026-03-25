database = {}


def store_value(key, value):
    database[key] = value


def get_value(key):
    return_value =  None
    if key in database:
        return_value = database[key]
    return return_value


def delete_value(key):
    if key in database:
        del database[key]
        return True
    return False


def list_keys():
    list_of_keys = []
    for key in database:
        list_of_keys.append(key)
    return list_of_keys
