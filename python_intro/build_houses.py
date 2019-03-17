import csv
import random

num_houses = 100
header = ['width', 'length', 'height', 'village']
with open('houses.csv', 'a') as db:
    writer = csv.writer(db)
    writer.writerow(header)
    for i in range(num_houses):
        row = [random.randint(20, 30), random.randint(10, 20), random.randint(5, 10), random.choice([0, 1])]
        writer.writerow(row)
