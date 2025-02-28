import json

def load_source(
    dir_path=None,
    level=None,
    current_level=None
    ):

    with open(f'{dir_path}/{str(level)}.json', 'r', encoding='utf-8') as jData:
        jdata = json.load(jData)
        if current_level:
            return jdata.get(str(current_level), 'Нет такого значения')
        else:
            return jdata

