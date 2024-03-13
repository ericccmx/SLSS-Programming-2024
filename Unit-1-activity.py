# Class Mark Calculator
# Author: Eric Zhang
# Date: Mar 4th, 2024

# Ask for the user's name.
# Greet the user with their name, and tell them how this mark calculator works.
user_name = input("Welcome to class mark calculator designed by Eric. What's your name?")
print(f"Before we start, {user_name}, let me tell you how this mark calculator works. I'll ask the marks that you received on your quizzes, tests, and projects; I'll then ask their weightage percentages respectively. I'll finally tell you your final calculated mark. ")

# Create a function to obtain what the user gets on their quizzes.
def quiz_to_float(quiz):
    return float(quiz)

# Create a function to obtain the weightage percentage of quizzes.
def quiz_weightage_to_float(quiz_weightage):
    return float(quiz_weightage)/100

# Create a function to obtain what the user gets on their tests.
def test_to_float(test):
    return float(test)

# Create a function to obtain the weightage percentage of tests.
def test_weightage_to_float(test_weightage):
    return float(test_weightage)/100

# Create a function to obtain what user gets on their projects.
def project_to_float (project):
    return float (project)

# Create a function to obtain the weightage percentage of projects.
def project_weightage_to_float(project_weightage):
    return float(project_weightage)/100

# Ask and calculate the weighted quiz mark.
def quiz():
    quiz = quiz_to_float(input("What did you get on your quizzes?"))
    quiz_weightage = quiz_weightage_to_float(input("What is the weightage percentage of these quizzes?"))
    quiz_final = quiz * quiz_weightage
    return quiz_final

# Ask and calculate the weighted test mark. 
def test():
    test = test_to_float(input("What did you get on your tests?"))
    test_weightage = test_weightage_to_float(input("What is the weightage percentage of these tests?"))
    test_final = test * test_weightage
    return test_final


# Ask and calculate the weighted project mark.
def project():
    project = project_to_float(input("What did you get on your project?"))
    project_weightage = project_weightage_to_float(input("What is the weightage percentage of these project?"))
    project_final = project * project_weightage
    return project_final

# Calculate and give the final combined mark.
def final():
    final = quiz() + test() + project()
    if final >=86:
        print(f"Nice job, {user_name}. You got {round (final, 2)}%!")
    elif final < 60:
        print(f"You really need to work on this course, {user_name}. You only got {round (final, 2)}%...")
    else:
        print(f"You did okay, {user_name}. You got {round (final, 2)}%.")

final()