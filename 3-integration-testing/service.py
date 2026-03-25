from datastore import store_value, get_value, delete_value as del_val, list_keys

def process_and_store(key, raw_value):
    raw_value = raw_value.strip().upper()
    store_value(key, raw_value)
    return raw_value


def retrieve_processed(key):
    return_value =  None
    if get_value(key):
        return_value = get_value(key).lower()
    return return_value


def update_value(key, raw_value):
    process_and_store(key, raw_value)


def delete_value(key):
    return del_val(key)


def list_all_keys():
    return list_keys()
