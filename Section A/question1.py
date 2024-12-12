# Part(i)
def calculate_area(r):
    pie = 3.14
    area_of_a_circle = pie*r**2
    print(f"The area of a circle is {area_of_a_circle:.2f}")
print(calculate_area(4))

#Part(ii)
integers = [4,7,2,9,12,15]
sum_of_odd = 0                                                          
for integer in integers:
    if integer % 2 != 0:
        sum_of_odd += integer
    print(f"The sum of odd numbers is {sum_of_odd}")

#Part(iii)
def operation():
    number1 = int(input("Enter your number one value: "))
    number2 = int(input("Enter your number2 value: "))
    print(number1 + number2)
    print(number1 - number2)
    print(number1 * number2)
    print(number1 / number2)
operation()

#Part(v)
student_info = {"name":"Alice","age":20,"grade":"A"}
student_info["age"]=26
print(student_info)
student_info["city"]="Kampala"
print(student_info)
