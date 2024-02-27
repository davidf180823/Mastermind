# Mastermind Game

This is a Python implementation of the classic Mastermind game, a logic puzzle where one player sets a secret code, and the other player tries to guess the code based on feedback provided after each guess.

## How to Play

1. **Initialize the Game:**
   - The game initializes with a secret code consisting of four randomly chosen colors from a predefined set.

2. **Make a Guess:**
   - The player makes guesses by entering a four-color code.
   - Colors are chosen from a set of possible colors: red, green, blue, white, orange, and grey.

3. **Feedback:**
   - After each guess, the player receives feedback in two categories:
      - `correctColorsAndPositions`: Number of colors that are correct and in the right position.
      - `correctColors`: Number of colors that are correct but in the wrong position.

4. **Winning the Game:**
   - The game continues until the player correctly guesses all colors and their positions.

## How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/mastermind-game.git
   cd mastermind-game

2. **Run the game:**
   ```bash
   python mastermind.py

3. **Follow the prompts to make guesses and enjoy the game!**
   ```rust
   Possible colors: red, green, blue, white, orange, grey

    Enter guess for position 1 (choose from red, green, blue, white, orange, grey): red
    Enter guess for position 2 (choose from red, green, blue, white, orange, grey): green
    Enter guess for position 3 (choose from red, green, blue, white, orange, grey): blue
    Enter guess for position 4 (choose from red, green, blue, white, orange, grey): white

    Guess 1: {'correctColorsAndPositions': 2, 'correctColors': 1}

    Enter guess for position 1 (choose from red, green, blue, white, orange, grey): red
    Enter guess for position 2 (choose from red, green, blue, white, orange, grey): blue
    Enter guess for position 3 (choose from red, green, blue, white, orange, grey): green
    Enter guess for position 4 (choose from red, green, blue, white, orange, grey): white
    
    Guess 2: {'correctColorsAndPositions': 3, 'correctColors': 0}
    
    ...
    
    Congratulations! You guessed the correct code.

Feel free to fork and modify the code to suit your preferences or add more features!
