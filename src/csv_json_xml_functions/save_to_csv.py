import csv
import os


def save_to_csv(directory_list: list, csv_file: str) -> None:
    print(directory_list)
    to_csv = directory_list
    keys = to_csv[0].keys()

    csv_file_exists = os.path.isfile(csv_file)

    with open(csv_file, 'a', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        if not csv_file_exists:
            dict_writer.writeheader()
            dict_writer.writerows(to_csv)
            print('CSV file created.')
        else:
            with open(csv_file, 'r') as read_file:
                report_nums = []
                for line in read_file.readlines():
                    array = line.split(',')
                    report_num = array[0]
                    report_nums.append(report_num)

                for row in to_csv:
                    exists = False
                    for num in report_nums:
                        exists = (row['report_num'] == num)
                        if exists:
                            print('filing is already listed.')
                            break

                    if not exists:
                        dict_writer.writerow(row)
                        print('New line of data added.')
