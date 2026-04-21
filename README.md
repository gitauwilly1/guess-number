# Guess the Number Game (with Difficulty Levels)

## Contributors
[William Gitau]
---

## Your Path to Interactive Gaming

The Guess the Number Game is an engaging, terminal-based gaming application designed to challenge players' logical thinking and deduction skills. It provides a structured yet entertaining number-guessing experience through multiple difficulty tiers: **Choose → Deduce  → Conquer**.

---

## Problem Statement

Many casual games lack the perfect balance between challenge and accessibility, leading to:
- Games that are either too easy (boring) or too hard (frustrating) with no middle ground
- Lack of progress tracking and competitive motivation
- Absence of helpful guidance when players get stuck
- No persistence of achievements across gaming sessions

---

## Solution Overview

This application provides a guided evaluation journey:

| Phase | Description |
|-------|-------------|
| **Choose** | Players select their preferred difficulty level (Easy, Medium, Hard) with varying attempt limits |
| **Deduce** | Interactive guessing with real-time "Too High" or "Too Low" feedback and intelligent hints |
| **Conquer** | Score calculation based on performance, persistent leaderboard tracking, and replayability options |

---

## Key Features

- **Dynamic Difficulty System** - Three distinct difficulty levels (Easy: 10 tries, Medium: 7 tries, Hard: 5 tries) that adjust the challenge intensity.

- **Smart Hint Mechanism** - After 3 incorrect guesses, the game provides contextual clues about the number's properties (even/odd, divisibility, range).

- **Persistent Leaderboard** - Saves player names and scores to a local text file, displaying the top 5 performers across all sessions.

- **Adaptive Scoring Algorithm** - Calculates scores based on attempts used and difficulty multiplier, rewarding efficient guessing.

- **Modular Object-Oriented Design** - Clean, extensible architecture that separates game logic, scoring, and file operations.

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python 3** | Core game logic, flow control, and user interaction |
| **Random Module** | Secure random number generation for unpredictable gameplay|
| **Datetime Module** | Timestamp generation for score tracking |
| **OS Module** | File system operations for leaderboard persistence|
| **Standard I/O** | 	Terminal-based input/output handling |

---

## Installation & Setup
To deploy this project locally, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/gitauwilly1/guess-number.git](https://github.com/gitauwilly1/guess-number.git)

2. **Navigate into the directory:**
   ```bash
   cd guess-number

3. **Execution: Run the application script:**
   ```bash
   python guess_number.py

---



## Known Bugs

There are no known bugs.



---



## License

* **License:** MIT License.



---



## Support and Information

**Email:** [gitauwilly254@gmail.com]