import csv


def csv_reader(file_name):
    fieldnames = ['user_id', 'title', 'story', 'criteria', 'value', 'estimation', 'status']
    with open(file_name, "r") as csv_file:
        text = csv.DictReader(csv_file, fieldnames=fieldnames)
        text_list = list(text)
        return text_list


def route_form():
    text_list = csv_reader("data.csv")
    print(text_list)

route_form()