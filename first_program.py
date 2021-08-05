# defining function taking in a phrase assigining variable then capitalizing the first letter of the phrase making capitalized phrase 

# if phrase starts with interrogatives then it will return with the first letter capitalized other wise it will return with capitalized without question mark

# if the user types in /end it will end the loop and print out what the user input stored in the empty list results 

def sentence_maker(phrase):
    interrogatives = ("how", "what", "why")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

results = []

while True:
    user_input = input("Say something: ")   
    if user_input == "/end":
        break
    else:
        results.append(sentence_maker(user_input))

print(" ".join(results))        

