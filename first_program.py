# defining function taking in a phrase assigining variable then capitalizing the first letter of the phrase making capitalized phrase 

# if phrase starts with interrogatives then it will return with the first letter capitalized other wise it will return with capitalized without question mark

# if the user types in /end it will end the loop and print out what the user input stored in the empty list results 

# def sentence_maker(phrase):
#     interrogatives = ("how", "what", "why")
#     capitalized = phrase.capitalize()
#     if phrase.startswith(interrogatives):
#         return "{}?".format(capitalized)
#     else:
#         return "{}.".format(capitalized)

# results = []

# while True:
#     user_input = input("Say something: ")   
#     if user_input == "/end":
#         break
#     else:
#         results.append(sentence_maker(user_input))

# print(" ".join(results))        

# temps = [221, 234, 340, -9999, 230]

# new_temps = [temp / 10 if temp != -9999 else 0 for temp in temps]

# print(new_temps)

# function that takes parameter a list that contains both numbers and strings if item in list is a string it wil return zero if item is int it will return the vaule

# def foo(lst):
#     return [i if not isinstance(i, str)
#         else 0 for i in lst ]



# print(foo(['zach', 89, 'rachel', 89, 67])
# )


# a function that takes a list as paremter and returns the stings as floats and gives the user a sum of those floats
# def foo(lst):
#     return sum([float(i) for i in lst])

# print(foo(['5.6', '5.6']))    

# def mean(*args):
#     return sum(args) / len(args)


# print(mean(1, 3, 4))    

# def foo(*args):
#     return sum(args) / len(args)

# print(foo(10,20,30,40))
# 

# a function that takes an indefinite number of arguments then returns the argument all uppercase and sorts them from first to last alphabetical order (not a band reference )
# def foo(*args):
#     args = [x.upper() for x in args]
#     return sorted(args)

# print(foo('stupid', 'arrogant', 'zach', 'rachel'))      

# opens text file ARG IS FILEPATH
# myfile = open("fruit.txt")
# # you can save the content in a varible
# content = myfile.read()
# # closes file so its not stored in RAM
# myfile.close()

# using with to open myfile and the defining the function inside of it...automatically closes file at end of function same as above function just more effiecent and dry
# with open("fruit.txt") as myfile:
#     content = myfile.read()

# print(content)

# creating and writing tomatoe to new file \ creates new line
# with open("files.vegetables.txt", "w") as myfile:
#     myfile.write('Tomatoe')
#     myfile.write('\nOnion\nCucumber\nGarlic')


# opening the bear.txt file
# myfile = open('bear.txt')
# # reading the bear.txt file and storing it in varible content
# content = myfile.read()
# # closing the file to free up storage in RAM
# myfile.close()
# # printing the first 90 characters of file
# print(content[:90])

# a functoin that gets a single string character and a filepath as parameters
# then opens the file path, reads the file, and returns the occurences of the character 
# def foo(character, filepath="bear.txt"):
#     file = open(filepath)
#     content = file.read()
#     return content.count(character)

# print(foo('e', 'bear.txt'))   


# opens bear.txt saves it to content variable then closes file then saves the first 90 characters of that to new varible char
# myfile = open('bear.txt')
# content = myfile.read()
# myfile.close()
# char = content[:90]


# # creating a new file called first.txt with writing permission as newfile then writing the first 90 characters of the bear text to it from the char varible
# with open('first.txt', 'w') as newfile:
#     newfile.write(char)

# # \n is a break line