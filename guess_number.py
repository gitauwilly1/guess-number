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
        
        print(f"\n HINT: {', '.join(hints[:2])}")
        self.hint_given = True

    def calculate_score(self, attempts_used):
        """Calculate score based on attempts used and difficulty"""
        base_score = 1000
        difficulty_multiplier = {'easy': 1, 'medium': 2, 'hard': 3}
        
        score = (base_score - (attempts_used * 50)) * difficulty_multiplier[self.difficulty]
        return max(score, 100)
    
    def save_high_score(self, username, score):
        """Save high score to file"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open(self.scores_file, 'a') as file:
            file.write(f"{username},{score},{self.difficulty},{timestamp}\n")
        
        print(f" Score saved to {self.scores_file}")

    def display_leaderboard(self):
        """Display top 5 high scores"""
        if not os.path.exists(self.scores_file):
            print("\n No high scores yet! Be the first!")
            return
        
        print("\n" + "="*60)
        print(" LEADERBOARD - TOP 5 SCORES ")
        print("="*60)
        print(f"{'Rank':<6} {'Player':<15} {'Score':<10} {'Difficulty':<12} {'Date':<20}")
        print("-"*60)
        
        try:
            with open(self.scores_file, 'r') as file:
                scores = []
                for line in file:
                    try:
                        username, score, difficulty, timestamp = line.strip().split(',')
                        scores.append((username, int(score), difficulty, timestamp))
                    except:
                        continue
                
                
                scores.sort(key=lambda x: x[1], reverse=True)
                
               
                for i, (username, score, difficulty, timestamp) in enumerate(scores[:5], 1):
                    print(f"{i:<6} {username:<15} {score:<10} {difficulty.capitalize():<12} {timestamp[:10]:<20}")
                
        except Exception as e:
            print(f"Error reading scores: {e}")
        
        print("="*60)


    def play_round(self):
        """Play one round of the game"""
        self.generate_number()
        attempts_used = 0
        guesses = []
        
        print(f"\n I'm thinking of a number between 1 and 100...")
        print(f"You have {self.remaining_tries} attempts remaining.")
        
        while self.remaining_tries > 0:
            try:
                guess = input(f"\n Enter your guess ({self.remaining_tries} left): ").strip()
                
                if not guess.isdigit():
                    print(" Please enter a valid number!")
                    continue
                
                guess = int(guess)
                
                if guess < 1 or guess > 100:
                    print(" Please guess a number between 1 and 100!")
                    continue
                
                if guess in guesses:
                    print(" You already guessed that number! Try a different one.")
                    continue
                
                guesses.append(guess)
                attempts_used += 1
                self.remaining_tries -= 1
                
                # Check guess
                if guess == self.secret_number:
                    score = self.calculate_score(attempts_used)
                    print(f"\n CONGRATULATIONS! You guessed it in {attempts_used} attempts!")
                    print(f" The number was: {self.secret_number}")
                    print(f" Your score: {score}")
                    
                    
                    username = input("\nEnter your name for the leaderboard: ").strip()
                    if username:
                        self.save_high_score(username, score)
                    
                    return True
                
                elif guess < self.secret_number:
                    print(" Too LOW! Try a higher number.")
                else:
                    print(" Too HIGH! Try a lower number.")
                
                
                if attempts_used == 3 and not self.hint_given:
                    self.give_hint()
                
                
                if self.remaining_tries > 0:
                    print(f" {self.remaining_tries} attempts remaining.")
                
            except ValueError:
                print(" Invalid input! Please enter a number.")
            except KeyboardInterrupt:
                print("\n\n Game interrupted. Goodbye!")
                return False
        
        
        print(f"\n GAME OVER! You've run out of attempts.")
        print(f" The number was: {self.secret_number}")
        return False
    
    def play_again(self):
        """Ask if user wants to play again"""
        while True:
            choice = input("\n Play again? (y/n): ").lower().strip()
            if choice in ['y', 'yes']:
                return True
            elif choice in ['n', 'no']:
                return False
            else:
                print("Please enter 'y' or 'n'")


    def run(self):
        """Main game loop"""
        self.display_welcome()
        
        while True:
            self.choose_difficulty()
            self.play_round()
            self.display_leaderboard()
            
            if not self.play_again():
                print("\n Thanks for playing! Goodbye!")
                break
            
            print("\n" + "="*50)
            print(" NEW GAME STARTING... ")
            print("="*50)


if __name__ == "__main__":
    game = GuessTheNumber()
    game.run()