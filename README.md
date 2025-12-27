# GUESS-THE-NUMBER

A fun Guess The Number game built using Python.
This project includes two versions of the game:

🖥️ GUI version using Tkinter.

⌨️ Console version using standard input/output.

Players choose a difficulty level and try to guess a randomly generated number within limited attempts.

📂 Project Files:
Guess-The-Number/

├── GAME GUI.py          # GUI version using Tkinter

├── Guess The Number.py  # Console-based version

├── GAME LOGO.png        # Game icon/logo

└── README.md            # Project documentation

🎮 Game Rules:

- The computer generates a random number between 1 and 100.
- Choose a difficulty level: Easy → 7 attempts; Medium → 5 attempts; Hard → 3 attempts.
- After each wrong guess, you’ll get a hint: Too High or Too Low.
- The game ends when: 
  You guess the correct number ✅.
  You run out of attempts ❌.

🖥️ GUI Version (Tkinter):
✨ Features:

- Modern multi-screen interface (Menu, Rules, Game).
- Difficulty selection.
- Attempts counter.
- Restart, Back, and Exit buttons.
- Entry disabled after game ends (clean UX).

▶️ How to Run
python "GAME GUI.py"

[Make sure GAME LOGO.png is in the same folder].

⌨️ Console Version:
✨ Features:

- Simple terminal-based gameplay
- Difficulty selection
- Hint system
- Replay option after game over

▶️ How to Run
python "Guess The Number.py"

🛠️ Requirements:

- Python 3.14.0
- Tkinter (comes pre-installed with Python)
- emoji module (for GUI version)
  Install emoji if needed:
  pip install emoji

🧠 Concepts Used:

- Python functions.
- Conditional logic.
- Loops.
- Exception handling.
- Random number generation.
- Tkinter GUI (Frames, Buttons, Labels, Entry).
- State management (enable/disable widgets).

👨‍💻 Author:

Yash,
Beginner-friendly Python project for learning logic + GUI development.

⭐ If you like this project, don’t forget to star the repository on GitHub!
