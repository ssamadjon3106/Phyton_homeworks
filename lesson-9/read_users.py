import csv


with open('/Users/samadjon/Phyton_homeworks-3/lesson-9/usernames.csv', 'rt') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        print(row)

