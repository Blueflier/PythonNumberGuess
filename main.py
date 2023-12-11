#!/usr/bin/env python3

class NumberGuesser():
    def __init__(self, lower_bound, upper_bound):

        self.ori_lower_bound = lower_bound
        self.ori_upper_bound = upper_bound
        #you can call functions in the instantiation
        self.reset()
        self.run()

    def lower(self, guess):
        self.upper_bound = guess - 1

    def higher(self, guess):
        self.lower_bound = guess + 1

    def reset(self):
        self.lower_bound = self.ori_lower_bound
        self.upper_bound = self.ori_upper_bound  
        self.remaining_guesses = 7

    def getCurrentGuess(self):
        return (self.lower_bound + self.upper_bound) // 2

    def run(self):
        print("Think of a number between 1 and 100.")
        while self.remaining_guesses > 0:
            guess = self.getCurrentGuess()
            print(f"Is the number {guess}? (h/l/c/r): ")
            input_1 = input().lower()

            if input_1 == "h":
                self.higher(guess)
            elif input_1 == "l":
                self.lower(guess)
            elif input_1 == "c":
                print(f"You picked {guess}? Great pick.")
            elif input_1 == "r":
                self.reset()
            self.remaining_guesses -= 1

# Add/remove/rearrange statements in this method as you wish
def main():
  # Don't change the function main()
  first = NumberGuesser(1, 100)
  print(first.getCurrentGuess())
#   second = NumberGuesser(1, 100)
#   second.getCurrentGuess()
#   third = NumberGuesser(1, 100)
#   third.getCurrentGuess()
#   fourth = NumberGuesser(1, 100)
#   fourth.getCurrentGuess()
#   fifth = NumberGuesser(1, 100)
#   fifth.getCurrentGuess()


main()