""" Learn Recursion """

import json
from pprint import pprint

def my_recursive(items) -> str:
    """ Print Elements """
    for item in items:
        print(f"Easy Name: {item['name']}")
        print(f"Unique ID: {item['UID']}")
        print(f"Parent ID: {item['PID']}")

        if len(item['children']) == 0:
            print(f"{item['name']} has no children")
            # return my_recursive(item['children'])
            # return item
        else:
            print(f"{item['name']} has {len(item['children'])} children")
            my_recursive(item['children'])
            # print("")
            # return item


def get_obj_by_id(list_items, query) -> dict:
    """ Get an object from data set by ID """

    for item in list_items:
        if item["UID"] == query:
            print(f'*** Item Is *** : {item}')
            return item
        else:
        # elif item["children"] != []:
            items = item["children"]
            return get_obj_by_id(items, query)


with open('calendar.json', 'r', encoding='utf-8') as file:
    json_content = json.load(file)
    list_to_process = json_content["favorites"]
    pprint(get_obj_by_id(list_to_process, "m3-w1"))
    # pprint(my_recursive(list_to_process))
