import csv

input_path = '/Users/samadjon/Phyton_homeworks-3/lesson-9/homework/grades.csv'
output_path = '/Users/samadjon/Phyton_homeworks-3/lesson-9/homework/average_grades.csv'

def calculate_average_grades():
    subject_totals = {}
    subject_counts = {}

    with open(input_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            subject = row['Subject']
            grade = int(row['Grade'])

            if subject not in subject_totals:
                subject_totals[subject] = 0
                subject_counts[subject] = 0

            subject_totals[subject] += grade
            subject_counts[subject] += 1

    averages = {subject: round(subject_totals[subject] / subject_counts[subject], 1) for subject in subject_totals}

    print("Averages calculated:", averages)

    with open(output_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Subject', 'Average Grade'])
        for subject, average in averages.items():
            writer.writerow([subject, average])

    print("Averages written to", output_path)

calculate_average_grades()


