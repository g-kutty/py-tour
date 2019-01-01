import csv

big_list = [
    {
        'name': 'Fredrick Stein',
        'userid': 6712359021,
        'is_admin': False
    },
    {
        'name': 'Wiltmore Denis',
        'userid': 2525942,
        'is_admin': False
    }
]


with open('output.csv', 'w') as output_csv:
    fields = ['name', 'userid', 'is_admin']
    output_writer = csv.DictWriter(output_csv, fieldnames=fields)

    output_writer.writeheader()
    for item in big_list:
        output_writer.writerow(item)
