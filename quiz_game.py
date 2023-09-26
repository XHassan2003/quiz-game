print("Wellcome to Quiz game!")
name = input("Enter your name: ")
start = input("Do you want to play (yes/no): ")
if start.lower() != "yes":
    quit()
print("Lets play!")
score = 0
question = input("What is the capital of Spain: ")
if question.lower() == "madrid":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
question = input("What is the currency of Spain: ")
if question.lower() == "euro":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
question = input("What is the capital of England: ")
if question.lower() == "london":
    print("Correct!")
    score += 1
else:
    print("Incoreect!")
question = input("What is the currency of England: ")
if question.lower() == "pound":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
question = input("In which continent Spain is situated: ")
if question.lower() == "europe":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
print("Your score is: " + str(score))
print("You got: " + str((score/5) * 100)+ "%." )
print("Thanks for playing!")                    
