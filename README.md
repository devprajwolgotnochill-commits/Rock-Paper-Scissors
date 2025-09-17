# Rock-Paper-Scissors Game 🪨📄✂️

A simple command-line **Rock-Paper-Scissors** game in Python where you can play against the computer.

---

## Features

- Choose between **rock**, **paper**, or **scissors**.
- Play against a computer that makes a random choice.
- Displays the result: **Win**, **Lose**, or **Draw**.
- Friendly terminal messages showing both your and computer's choices.

---

## How to Play

1. Run the Python script:

```bash
python rock_paper_scissors.py
```

2. Enter your choice when prompted:

```
ENTER ROCK, PAPER, SCISSOR:
```

3. The game will display:

- Your choice
- Computer's choice
- Result (WIN / LOSE / DRAW)

---

## Game Logic

- Rock beats Scissors
- Scissors beat Paper
- Paper beats Rock
- Same choices result in a draw

---

## Example

```
ENTER ROCK, PAPER, SCISSOR: rock
You chose rock and computer chose scissors : WIN
```

```
ENTER ROCK, PAPER, SCISSOR: paper
DRAW :DRAW
```

---

## Requirements

- Python 3

No external libraries needed (uses built-in `random` and `sys` modules).

---

## Notes

- Only the first letter of the choice is used internally for comparison (`r`, `p`, `s`).
- Input is case-insensitive.

