import csv
f = open("student.csv","w",newline="")
s = csv.writer(f)
s.writerow(["studentid","rollno","name","mobile no"])
studentid = (input("enter a studentid:"))
rollno = (input("enter a rollnno:"))
name = input("Enter a student name:")
mobile_no = input("enter your mobile number:")
s.writerow(["studentid,rollno,name,mobile no"])
print("student record has saved:")


