import csv
fields = ['Name', 'Total_Marks']
rows = [
    ['Saurav Shrestha', '73'],
    ['Sarrok Magar', '75'],
    ['Bibek Tamang', '48'],
    ['Prakash Gurung', '70'],
    ['Sujal Maharjan', '57']  
]

with open("records.csv", 'w', newline="") as records:
    csvwriter = csv.writer(records)        
    csvwriter.writerow(fields)            
    csvwriter.writerows(rows)