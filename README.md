Number Game

This is a Python-based number game that allows users to test their arithmetic skills by answering randomly generated math questions. Users can choose an operator, and the game will quiz them with five math questions. After answering, the program provides feedback and calculates the user's score.

Features

The game allows users to select from four basic arithmetic operations: + (addition), - (subtraction), * (multiplication), and / (division).

The program generates five random math questions using the selected operator.

After each answer, the game provides immediate feedback (whether the answer is correct or not).

A score is calculated based on the user's correct answers, and a final evaluation is displayed.

Error handling is included to ensure valid user inputs (e.g., handling non-numeric inputs).


How to Play

1. When the game starts, you'll be prompted to choose if you want to play the game.


2. If you choose "yes", you'll be asked to pick an operator (+, -, *, /).


3. The game will generate five math questions based on the chosen operator.


4. After each question, you'll input your answer, and the game will let you know if you're correct.


5. After answering all five questions, the game will show your final score and give feedback:

If you get 4 or 5 correct answers, you’ll receive a “Well done” message.

If you get 2 or 3 correct answers, you’ll get a “Better luck next time” message.

If you get 1 or fewer correct answers, it encourages you to keep practicing.



6. You'll be asked if you want to play again. If you say "no", the game will exit with a goodbye message.



Example Gameplay

Welcome to the Number Game!
Do you want to play the math quiz? (yes/no): yes
Choose an operator (+, -, *, /): +
Question 1: What is 4 + 5? 9
Correct! Well done!

Question 2: What is 3 + 6? 7
Wrong answer! The correct answer was 9.

...

Your final score is: 4/5
Well done! You did a great job!
Do you want to play another round? (yes/no): no
Thank you for playing! Goodbye!

Requirements

Python 3.x installed on your system.

A terminal or command-line tool to run the Python script.


How to Run the Game

1. Clone the repository or download the Python file.


2. Open your terminal (or command prompt) and navigate to the folder containing the Python file.


3. Run the following command:

python number_game.py


4. Follow the instructions in the terminal to play the game.



Error Handling

If you enter non-numeric input when answering questions, the game will prompt you to enter a valid number.

