# Python Quiz game
# Declare all the collections and variables we will need 
# We need a Tuple of questions, a 2D tuple of options
# I will have 5 questions, but you need to have 15 
# It will also have a tuple of answers
# There will be list of guesses so we can expand our list

# There will be these variables
# score set to 0
# question_num to keep track of what number question we are on

# Begin with questions

# Animal Python Quiz
questions = ("What is the fastest land animal? ",
             "What is the fastest flying animal? ",
             "What is the fastest marine animal? ",
             "What is a group of lions called? ",
             "What is the largest fish? ",
             "What is the largest mammal? ",
             "Which mammal has the most powerful bite? ",
             "How many tentacles does a octopus have? ",
             "What is the only mammal capable of flight? ",
             "What is the smallest mammal? ",
             "What is a group of cows called? ",
             "What is a group of fish called? ",
             "What is a baby kangaroo called? ",
             "What is the most venomous fish? ",
             "What kind of fish is Nemo from 'Finding Nemo'? ")

# 2D Tuple of options - 4 for every question
# Tuple will have 4 elements

"""options =((), first element corresponds to first quesiton
            (), corresponds to 2nd question
            (), corresponds to 3rd question
            ()), corresponds to 4th question"""

options = (("A. Cheetah B. Tiger C. Jaguar D. Black panther",),
           ("A. Vulture B. Seagull C. Pegerine Falcon D. Golden Eagle",),
           ("A. Swordfish B. Sailfish C. Blue whale D. Dolphin ",),
           ("A. pride B. herd C. school D. shiver ",),
           ("A. Whale shark B. Blue whale C. Tiger shark D. Great white shark ",),
           ("A. Blue whale B. Polar bear C. Moose D. Giraffe ",),
           ("A. Hippopotamus B. Saltwater crocodile C. Jaguar D. Grizzly bear ",),
           ("A. 2 B. 7 C. 9 D. 8",),
           ("A. Bats B. Flying squirrel C. Flying fish D. Flying snakes ",),
           ("A. Bumblebee bat B. Mouse lemur C. Pygmy possum D. Etruscan shrew ",),
           ("A. herd B. school C. mob D. streak ",),
           ("A. school B. mob C. shiver D. streak ",),
           ("A. Joey B. Calf C. Monkey D. Bear ",),
           ("A. Pufferfish B. Piranha C. Lionfish D. Stonefish ",),
           ("A. Clownfish B. Salmon C. Catfish D. Swordfish ",
           ))

#answers and guesses

answers = ("A", "C", "B", "A", "A", "A", "B", "D", "A", "A", "A", "A", "A", "D", "A")
guesses = []

score = 0
question_num = 1

for i in range(len(questions)):
    print("Question ", question_num, ": ", questions[i], sep="")
    for j in options[i]:
        print(j)
    guess = input("Enter your answer: ").upper()
    guesses.append(guess)
    if guess == answers[i]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect.")
    question_num += 1

print("Final Score:", score, "/", len(questions))


