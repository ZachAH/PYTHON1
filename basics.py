# day_hours = 24
# week_days = 7

# week_hours = day_hours * week_days
# print(week_hours)

# different types integer, string, float
# x = 10
# y = '10'
# z = 10.1

# print(type(x), type(y), type(z))

# adding numbers together and printing out
# x = 10
# y = 25
# z = 25
# s = x + y + z

# print(s)


# anything in [is called a list] lists can contain other lists ["zach", [28, 156.5]]
# student_grades = [9.1, 8.8, 7.5]
# max_value = max(student_grades)
# print(max_value)


#listing number of times 10.0 occured in list
# student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
 
# list_10 = student_grades.count(10.0)
 
# print('10.0 occured', list_10, 'times in list')

# mysum = sum(student_grades)
# length = len(student_grades)
# mean = mysum / length
# print(mean)


#returns string to uppercase it is method so needs to be called with ()
# zach = 'hello'.upper()
# print(zach)

# RANGE CREATES A LIST OF NUMBERS
# list(range(1,10)) will output [1,2,3,4,5,6,7,8,9]
#list(range(1, 10, 2)) will output [1,3,5,7,9] counts happens every two items starting at one and ending at 9

# monday_tempetures = [9.1, 8.8, 7.5]
# student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}

# mysum = sum(student_grades.values())
# length = len(student_grades)
# mean = mysum / length
# print(mean)
# print(student_grades.keys())

# TUPLES are inmutable and lists are mutable can't append or remove from tuples
# monday_tempetures = (1, 4, 5)

# #list
# monday_tempetures = [9.1, 8.8, 7.5]
# # print(monday_tempetures)
# #appends to end of list
# monday_tempetures.append(8.1)
# # print(monday_tempetures)
# #clears list
# # monday_tempetures.clear()

# print(monday_tempetures.index(8.8))

# seconds = [1.2323442655, 1.4534345567, 1.023458894]
# current = 1.10001399445
# seconds.append(current)

# monday_tempetures = [9.1, 8.8, 7.5]

# def mean(mylist):
#     the_mean = sum(mylist) / len(mylist)
#     return the_mean

# print(mean([1, 4, 6]))

# def calculate_length(lst):
#     return len(lst)

# print(calculate_length([5, 6, 6, 9, 8, 7]))   
# 
# def mult(a):
#     return a * a
# print(mult(4))    

# def conv(a):
#     return a * 29.57353
# print(conv(2))    

# def mean(value):
#     if type(value) == dict:
#         the_mean = sum(value.values()) / len(value)
#     else:
#             the_mean = sum(value) / len(value)

#     return the_mean 

# def mean(value):
#     if isinstance(value, dict):
#         the_mean = sum(value.values()) / len(value)
#     else:
#             the_mean = sum(value) / len(value)

#     return the_mean   
# 

#  IF LENGTH OF PASSWORD IS GREATER OR EQAUL TO 8 IT WILL PRINT TRUE OTHERWISE IT WILL PRINT FALSE 
def foo(password):
    if len(password)  >=8  :
        return True
    else :
        return False

print(foo('zacharyouiiou'))        
