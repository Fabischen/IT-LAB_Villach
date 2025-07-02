import random # Import random module

def trainer():
  try: rounds = int(input("How many rounds would you like to play?")) # Ask user how many rounds they want
  except ValueError: print("Please enter a valid number."); return    # Handle invalid input, exit function if input is invalid

  correct = 0, wrong = 0 # Initialize counters for correct and wrong answers

  for i in range(rounds): # Loop through the number of rounds
    # Generate two random numbers between 1 and 10
    n1 = random.randint(1, 10)
    n2 = random.randint(1, 10)
    result = n1 * n2 # Calculate correct result

    # Ask user for their answer
    print(f"\nRound {i+1}: What is {n1} x {n2}?")

    try:
      # Users answer input
      answer = int(input("Your answer: "))

      # Check if answer is correct
      if answer == result: print(f"Correct! Your answer {answer} is right."); correct += 1
      else: print(f"Incorrect! The correct answer is {result}."); wrong += 1
    except ValueError:
      
      # Handle non-integer input
      print(f"Invalid input! The current answer was {result}."); wrong += 1

  # Show current results after each round
  print(f"\nResult: {correct}/{rounds} correct.")
  print(f"Wrong are {wrong} answers!")
  print("Great job! Keep practing!")

trainer() # Call the function to start the program