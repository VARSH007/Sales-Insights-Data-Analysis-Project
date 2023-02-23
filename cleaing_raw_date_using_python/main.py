'''
import csv
with open('full.csv', 'r') as input_file, open('var.csv', 'w') as output_file:
    input_data = input_file.read().replace('),(', ')\n(')
    output_file.write(input_data)
'''


import csv
from datetime import datetime

with open('var.csv', 'r') as input_file, open('finalfile.csv', 'w', newline='') as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)

    for row in reader:
        # Convert the date string to a datetime object
        row[3] = datetime.strptime(row[3].strip("'"), '%Y-%m-%d').date()
        # Write the row to the output file
        writer.writerow(row)

