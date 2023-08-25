import os
import json
import pandas

"""
This script is meant to be used with 溯洄/w4123's Genshin Voice.
Extracts and converts to csv.
"""


# Set the path to result.json
os.chdir("path/to/result.json")


data = {
    'name': [],
    'text': [],
}


with open('result.json', 'rt') as f:
    read_file = f.read()
    contents = json.loads(read_file)
    
    # Only change data_name 'Keqing' to whatever character
    data_name, data_type = 'Keqing', 'Dialog'

    for content in contents.values():
        try:
            if content['npcName'] == data_name and content['type'] == data_type:
                data['name'].append(content['npcName'])
                data['text'].append(content['text'])
        except KeyError:
            continue


if len(data['name']) > len(data['text']):
    data['name'].pop()


print(f"names: {len(data['name'])} text: {len(data['text'])}")


dataframe = pandas.DataFrame(data)
dataframe.head()
dataframe.to_csv('voicelines.csv', index=False)
