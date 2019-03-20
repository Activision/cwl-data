
import json
import os


event_match = []


def load_event(event_path):

    """helper function to import the structured data for every match of a specified tournament"""

    match_list = os.listdir(event_path)
    for x in match_list:
        with open('./{}{}'.format(event_path, x)) as i:
            file = json.load(i)
            event_match.append(file)

    return event_match


# example of use
EVENT = 'structured-2017-12-10-dallas/'
load_event(EVENT)

# 5th match in the list
print(event_match[5])

