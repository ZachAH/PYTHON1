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
def foo(lst):
    return sum([float(i) for i in lst])

print(foo(['5.6', '5.6']))    
