# Format: new_collection = [expression_evaluated_for_each_item for taco in current_collection if conditional]
# OR
# *result*  = [*transform* for *item* in *iteration* if *filter*]
# The conditional is optional

# These three examples do the same thing: loop through the stuff list and make a new list that contains the capitalized words.

#1 Good old for loop:
cap_stuff = []
for foo in cap_stuff:
  cap_stuff.append(foo.capitalize())
print(cap_stuff)

#2 Map using a lambda (an anonymous function):
cap_stuff = list(map(lambda foo: foo.capitalize(), stuff))
print(cap_stuff)