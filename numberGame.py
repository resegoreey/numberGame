import random

def math_quiz():
  #welcome the user to the game
  while True:
    #Ask the user if they want to play
    play = input("Would you like to test your math knowledge?(yes/no): ").lower()

    #quit the game is the answer is no
    if play != "yes":
      print("Sad to see you leave, Goodbye!")
      break

    #choose an operator
    while True:
      operator = input("Choose an operator(+, -, *, /): ")
      if operator in ['+', "-", "*", "/"]:
        break
      else:
        print("Invalid operator! Choose from +, - , * or /")

      #time for the game
    score = 0
    for i in range(5):
      #generate the numbers randomly
      num1 = random.randint(1, 100)
      num2 = random.randint(1, 100)

      #can't divide by zero!
      if operator == "/" and num2 == 0:
        num2 == random.randint(1, 100)
    #calculating the answer based on the operator
      if operator == "+":
        correct_ans = num1 + num2
      elif operator == "-":
        correct_ans = num1 - num2
      elif operator == "*":
        correct_ans = num1 * num2
      elif operator == "/":
        correct_ans = round(num1 / num2, 2)

    #handling errors and exceptions
      while True:
        try:
          user_ans = float(input(f"Question {i+1}: Calculate {num1} {operator} {num2} = "))
          break
        except ValueError:
          print("Invalid input: Please enter a number!")
        
      #checking for correct answers
      if user_ans == correct_ans:
        print("Excellent! You got it correct!")
        score += 1
      else:
        print(f"Incorrect! The answer is {correct_ans}, Keep practicing!")
      

        #final score
    print(f"You got {score}/5")
    if score >= 4:
        print("You did a great job! Keep it up!")
    else:
        print("Keep practising! You'll get there!")

      #ask the user if they want to play again
    while True:
        play_again = input("Do you want to continue playing? (yes/no): ").lower()
        if play_again in ["yes", "no"]:
          break
        else:
          print("Please type yes or no")

    if play_again != "yes":
        print("Thank you for playing! Goodbye!")
        break
math_quiz()




      
