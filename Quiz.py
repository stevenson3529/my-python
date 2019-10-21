#Quiz Program

#variables
score = 0
playing = 'n'

def guess_check(guess,answer):
    global score
    guesses = 0
    if(guess.lower() == answer.lower()):
        score = score + 1
        print('Correct! Your score is now ' + str(score))
    else:
        print("Incorrect. The answer was: " + answer + ". Your score is still " + str(score) + ".")

def final_check(guess,answer):
    global score
    if(guess.lower() == answer.lower()):
        score = score + 1
        playing = 'f'
    
print("Welcome to the quiz. There are 20 questions, split into 4 rounds of 5 questions. The categories are: Nature, Science, Computer Software and Hardware and General Knowledge. KEY TO ABBREVIATIONS: (1w) = The answer is 1 word. (5ch) = The answer is 5 characters long. Enjoy the quiz.")

print(" ")

playing = input("Would you like to start? (y/n)")
if playing == 'y':
    print(" ")
    
    print("Round 1: Nature")

    #Question 1
    print(" ")
    guess1 = input("Which type of bear lives in the North Pole? (2w)")

    guess_check(guess1,'Polar Bear')
    
    #Question 2
    print(" ")
    guess2 = input("Which is the fastest animal? (1w)")

    guess_check(guess2,'Cheetah')

    #Question 3
    print(" ")
    guess3 = input("What leaf does the canadian flag contain? (1w)")

    guess_check(guess3,'Maple')

    #Question 4
    print(" ")
    guess4 = input("What is the study of fossils called? (1w)")

    guess_check(guess4,"Paleontology")

    #Question 5
    print(" ")
    guess5 = input("What do penguins eat? (1w)")
    
    guess_check(guess5,"Plankton")
        
    #Round 2
    print(" ")
    print("Round 2:Science")

    #Question 6
    print(" ")
    guess6 = input("What is the lightest metal that exists? (1w)")

    guess_check(guess6,"Aluminium")

    #Question 7
    print(" ")
    guess7 = input("Who discovered penicillin? (2w)")

    guess_check(guess7,"Alexander Fleming")

    #question 8
    print(" ")
    guess8 = input("Around what pH does pure water have? (1ch)")

    guess_check(guess8,"7")

    #Question 9
    print(" ")
    guess9 = input("What is the 7th element on the periodic table? (1w)")

    guess_check(guess9,"Nitrogen")

    #Question 10
    print(" ")
    guess10 = input("What is felinology? (4w)")

    guess_check(guess10,'The study of cats')

    #Round 3
    print(" ")
    print("Round 3: Computer Software and Hardware")

    #Question 11
    print(" ")
    guess11 = input("What does VM stand for in computing? (2w)")

    guess_check(guess11,"Virtual Machine")

    #Question 12
    print(" ")
    guess12 = input("What is the open-source version of Google's Chrome browser called? (1w)")

    guess_check(guess12,"Chromium")

    #Question 13
    print(" ")
    guess13 = input ("What is the name of the browser Mozilla created? (1w)")

    guess_check(guess13,'Firefox')

    #Question 14
    print(" ")
    guess14 = input("What does CPU stand for? (3w)")

    guess_check(guess14,'Central Processing Unit')

    #Question 15
    print(" ")
    guess15 = input("What kernel does Microsoft's latest operating system, Windows 10, run on? (2w")

    guess_check(guess15,'Windows NT')

    #Round 4
    print(" ")
    print("Round 4:General Knowledge")

    #Question 16
    print(" ")
    guess16 = input("What is the longest river in the world? (1w)")

    guess_check(guess16,'Nile')

    #Question 17
    print(" ")
    guess17 = input("Who was the first female British Prime Minister? (2w)")

    guess_check(guess17,'Margaret Thatcher')

    #Question 18
    print(" ")
    guess18 = input("Which American city is nicknamed 'The Big Apple?' (2w)")

    guess_check(guess18,'New York')

    #Question 19
    print(" ")
    guess19 = input("Which country is the yen (¥) used in? (1w)")

    guess_check(guess19,'Japan')

    #Question 20
    print(" ")
    guess20 = input("In Morse code, what letter is a single dot? (1ch)")

    final_check(guess20,'e')


elif playing == 'f':
    print("Thank you for playing the quiz. You got " + str(score) + " out of 20 questions correct.")
elif playing == 'n':
    print("The user chose not to play the quiz.")
