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