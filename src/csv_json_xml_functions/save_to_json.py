import json
import os


def write_to_json(data, json_file: str) -> None:
    with open(json_file, 'w') as fp:
        json.dump(data, fp, sort_keys=True, indent=4)


def save_to_json(directory_list: list, json_file: str) -> None:

    json_file_exists = os.path.isfile(json_file)
    dict_list = directory_list
    append_json = []

    if not json_file_exists:
        write_to_json(dict_list, json_file)
        print('JSON file has been created.')
    else:
        with open('../sec_data_files/test.json', 'r') as read_json:
            append_json = json.load(read_json)

            for w_item in directory_list:
                exists = False
                for r_item in append_json:
                    exists = (r_item['report_num'] == w_item['report_num'])
                    if exists:
                        print('Entry already exists in JSON file.')
                        break
                if not exists:
                    append_json.append(w_item)
                    print('New entry added.')

        write_to_json(append_json, json_file)
        print('JSON file has been updated.')
