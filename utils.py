import json

def list_to_file(lst, filename):
    with open(filename, 'w') as f:
        for i in range(len(lst)):
            f.write(f'{lst[i]}\n')

def file_to_list(filename):
    with open(filename, 'r') as f:
        return f.read().splitlines()

def json_file_to_dict(filename):
    with open(filename) as f:
        return json.load(f)