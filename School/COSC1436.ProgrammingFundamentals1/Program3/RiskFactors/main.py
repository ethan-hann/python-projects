import csv
from tabulate import tabulate
import os


def check_file(file):
    if os.path.isfile(file):
        y = 1
        return y
    else:
        n = 0
        return n

file = input("What file is the data coming from? (don't forget extension): ")
no_valid_file = False

while not no_valid_file:
    if check_file(file) == 1:
        risk_file = open(file, "r")
        no_valid_file = True
    else:
        print("Invalid file name. Check to ensure the file exists and try again.")
        print("")
        file = input("What file is the data coming from? (don't forget extension): ")


reader = csv.reader(risk_file)

row_count = 0
risk_factors = []
heart_disease = []
motor_vehicle = []
teen_birth = []
adult_smoking = []
adult_obesity = []
state_names = []


for line in reader:
    if row_count >= 6:
        row = [line[0], float(line[1].strip("%")), float(line[5].strip("%")),
               float(line[7].strip("%")), float(line[11].strip("%")), float(line[13].strip("%"))]
        risk_factors.append(row)

    row_count += 1

for element in risk_factors:
    for index, item in enumerate(element):
        if index == 0:
            state_names.append(item)
        elif index == 1:
            heart_disease.append(item)
        elif index == 2:
            motor_vehicle.append(item)
        elif index == 3:
            teen_birth.append(item)
        elif index == 4:
            adult_smoking.append(item)
        elif index == 5:
            adult_obesity.append(item)

max_heart_disease = max(heart_disease)
max_motor_vehicle = max(motor_vehicle)
max_teen_birth = max(teen_birth)
max_adult_smoking = max(adult_smoking)
max_adult_obesity = max(adult_obesity)

min_heart_disease = min(heart_disease)
min_motor_vehicle = min(motor_vehicle)
min_teen_birth = min(teen_birth)
min_adult_smoking = min(adult_smoking)
min_adult_obesity = min(adult_obesity)

row1 = []
row2 = []
row3 = []
row4 = []
row5 = []

for element in risk_factors:
    if min_heart_disease == element[1]:
        row1 = ["Heart Disease Death Rate (2007)", element[0], min_heart_disease]
for element in risk_factors:
    if min_motor_vehicle == element[2]:
        row2 = ["Motor Vehicle Death Rate (2009)", element[0], min_motor_vehicle]
for element in risk_factors:
    if min_teen_birth == element[3]:
        row3 = ["Teen Birth Rate (2009)", element[0], min_teen_birth]
for element in risk_factors:
    if min_adult_smoking == element[4]:
        row4 = ["Adult Smoking (2010)", element[0], min_adult_smoking]
for element in risk_factors:
    if min_adult_obesity == element[5]:
        row5 = ["Adult Obesity (2010)", element[0], min_adult_obesity]


for element in risk_factors:
    if max_heart_disease == element[1]:
        row1.append(element[0])
        row1.append(max_heart_disease)
for element in risk_factors:
    if max_motor_vehicle == element[2]:
        row2.append(element[0])
        row2.append(max_motor_vehicle)
for element in risk_factors:
    if max_teen_birth == element[3]:
        row3.append(element[0])
        row3.append(max_teen_birth)
for element in risk_factors:
    if max_adult_smoking == element[4]:
        row4.append(element[0])
        row4.append(max_adult_smoking)
for element in risk_factors:
    if max_adult_obesity == element[5]:
        row5.append(element[0])
        row5.append(max_adult_obesity)

rows = [row1, row2, row3, row4, row5]
columns = ['Indicator', 'Minimum Value', '', 'Maximum Value', '']
print((tabulate(rows, columns, tablefmt="grid")))

best_and_worst = open('best_and_worst.txt', 'w')
best_and_worst.write((tabulate(rows, columns, tablefmt="grid")))
best_and_worst.close()
