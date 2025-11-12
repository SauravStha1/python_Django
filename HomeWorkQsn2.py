import csv


with open("records.csv", mode="r") as file:
    reader = csv.reader(file)
    header = next(reader)  

   
    passed_students = []

    for row in reader:
        name = row[0]
        marks = int(row[1]) 

        
        if marks > 60:
            passed_students.append([name, marks])
        else:
            pass 


with open("passed_students.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Total Marks"]) 
    writer.writerows(passed_students)

print(" passed_students.csv created successfully!")
