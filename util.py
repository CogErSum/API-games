import json

def json_to_dict(filename):
    try:
        with open(filename, 'r') as file:
            json_str = file.read()
            dict_list = json.loads(json_str)
        return dict_list
    except (TypeError, ValueError, IOError) as e:
        print(e)
