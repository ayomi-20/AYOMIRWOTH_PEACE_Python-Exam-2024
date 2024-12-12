#Part(i)
student_name = "Gloria Arinda"
student_number = "SEP23/BCS/088U/F"
programming = 90
data_science = 87
computer_applications = 77
total_subject_marks = programming+data_science+computer_applications
number_of_subjects = 3
average_mark = total_subject_marks/number_of_subjects
print(f"The student`s average mark is {average_mark:.3f}")

#Part(ii)
miles_driven = int(input("Enter the number of miles driven: "))
gallons_of_gas_used = int(input("Enter the gallons of gas used: "))
MPG = miles_driven/gallons_of_gas_used
print(f"The miles per gallon used by the car is {MPG} ")

#Part(iii)
for number in range(1,101):
    if number %2:
        print(number)