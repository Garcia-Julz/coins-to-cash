# # Here's the same thing written using a function that has been defined:
# def cap_string(foo):
#     return foo.capitalize()
  
# cap_stuff = list(map(cap_string, stuff))
# print(cap_stuff)

# #3 Comprehension
# cap_stuff = [foo.capitalize() for foo in stuff]
# print(cap_stuff)

# # Nested Comprehensions
# cap_stuff = [[item.capitalize() for item in foo] for foo in stuff]
# print(cap_stuff)

# An example of generating a new dictionary from an existing one:
grades = {
  "math": .56,
  "english": .65,
  "history": .74,
  "spanish": .83
}

# # In the new dictionary, the name of the subject (the key) is capitalized. The grade (the value) is multiplied by 100 and is now a string so we can have the % symbol.
# formatted_grades = { key.capitalize():f"{int(value*100)}%" for (key,value) in grades.items()}

#1 Good old for loop:
cap_stuff = []
for foo in grades:
  cap_stuff.append(foo.capitalize())
print(cap_stuff)

#2 Map using a lambda (an anonymous function):
cap_stuff = list(map(lambda foo: foo.capitalize(), grades))
print(cap_stuff)