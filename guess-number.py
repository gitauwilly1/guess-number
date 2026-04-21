import random
import os
from datetime import datetime

class GuessTheNumber:
    def __init__(self):
        self.difficulty_settings = {
            'easy': {'tries': 10, 'range': (1, 100)},
            'medium': {'tries': 7, 'range': (1, 100)},
            'hard': {'tries': 5, 'range': (1, 100)}
        }
        self.scores_file = "high_scores.txt"
        self.secret_number = None
        self.max_tries = None
        self.remaining_tries = None
        self.difficulty = None
        self.hint_given = False

         
    def display_welcome(self):
        """Display welcome message and game instructions"""
        print("\n" + "="*50)
        print("  GUESS THE NUMBER - WITH DIFFICULTY LEVELS  ")
        print("="*50)
        print("\n Instructions:")
        print("• I'll think of a number between 1 and 100")
        print("• You need to guess it within the given attempts")
        print("• I'll tell you if your guess is too high or too low")
        print("• Choose your difficulty wisely!")
        print("="*50)


    def choose_difficulty(self):
        """Let user choose difficulty level"""
        while True:
            print("\n Select Difficulty Level:")
            print("1. Easy   - 10 tries")
            print("2. Medium - 7 tries")
            print("3. Hard   - 5 tries")
            
            choice = input("\nEnter your choice (1/2/3): ").strip()
            
            if choice == '1':
                self.difficulty = 'easy'
                break
            elif choice == '2':
                self.difficulty = 'medium'
                break
            elif choice == '3':
                self.difficulty = 'hard'
                break
            else:
                print(" Invalid choice! Please enter 1, 2, or 3.")
        
        self.max_tries = self.difficulty_settings[self.difficulty]['tries']
        self.remaining_tries = self.max_tries
        print(f"\n {self.difficulty.upper()} mode selected! You have {self.max_tries} tries.")

     def generate_number(self):
        """Generate random number between 1 and 100"""
        self.secret_number = random.randint(1, 100)
        self.hint_given = False
    
    def give_hint(self):
        """Provide a hint after 3 wrong attempts"""
        if self.hint_given:
            return
        
        hints = []
        if self.secret_number % 2 == 0:
            hints.append("The number is even")
        else:
            hints.append("The number is odd")
        
        if self.secret_number % 5 == 0:
            hints.append("The number is divisible by 5")
        elif self.secret_number % 3 == 0:
            hints.append("The number is divisible by 3")
        
        if self.secret_number > 50:
            hints.append("The number is greater than 50")
        else:
            hints.append("The number is less than or equal to 50")
        
        print(f"\n💡 HINT: {', '.join(hints[:2])}")
        self.hint_given = True