

def make_family(name, **member):
    family_stuff = member.items()
    family_str = f"We are the {name} family. "
    for title, person in family_stuff:
        family_str += f"The {title} is {person}. "
    return family_str


the_shepherds = make_family("Shepherd", mom="Anne", dad="Joe", dog="Murph")
the_parkers = make_family("Parker", aunt="May", nephew="Peter")

print(the_shepherds)
print(the_parkers)


def calculate_average(subject, *test_scores, **student_details):
    # print("Type & value of subject: ", type(subject), subject)
    # print("Type & value of test_scores: ", type(test_scores), test_scores)
    # print("Type & value of the student_details: ", type(student_details), student_details)

    if subject == "English":
        average_score = 49
    else:
        average_score = sum(test_scores)/len(test_scores)
    
    print(f"{student_details['last_name']}, {student_details['first_name']} got an average score of {average_score} in {subject}.")


calculate_average("Math", 75, 64, 35, first_name="Bryan", last_name="Nilsen")
