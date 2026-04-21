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