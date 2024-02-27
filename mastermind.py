import random


class Mastermind:
    COLORS = ["red", "green", "blue", "white", "orange", "grey"]

    def __init__(self):
        # Initialize the secret code with four randomly chosen colors
        self.secret_code = random.sample(self.COLORS, 4)
        self.guess_count = 0  # Counter to keep track of the number of guesses

    def correctColorsAndPositions(self, colors):
        # Check how many colors are correct and in the right position
        return sum(1 for i in range(4) if colors[i] == self.secret_code[i])

    def correctColors(self, colors):
        # Check how many colors are correct but in the wrong position
        return sum(1 for color in colors if color in self.secret_code) - self.correctColorsAndPositions(colors)

    def guess(self, c1, c2, c3, c4):
        # Take a guess from the player and check the correctness
        colors = [c1, c2, c3, c4]
        self.guess_count += 1  # Increase the guess count

        correct_positions = self.correctColorsAndPositions(colors)
        correct_colors = self.correctColors(colors)

        # Return the result as a dictionary with category names
        result = {
            "correctColorsAndPositions": correct_positions,
            "correctColors": correct_colors
        }
        return result

    def display_possible_colors(self):
        print("Possible colors:", ", ".join(self.COLORS))


# Example of using the Mastermind class with user input and exceptions
if __name__ == "__main__":
    game = Mastermind()

    # Display possible colors to the user
    game.display_possible_colors()

    # Example of making guesses with user input and exception handling
    while True:
        try:
            user_guess = [
                input(f"Enter guess for position {i + 1} (choose from {', '.join(game.COLORS)}): ").lower()
                for i in range(4)
            ]

            if any(color not in game.COLORS for color in user_guess):
                raise ValueError("Invalid color entered. Please choose from the provided colors.")

            guess_result = game.guess(*user_guess)
            print(f"Guess {game.guess_count}: {guess_result}")

            if guess_result["correctColorsAndPositions"] == 4:
                print("Congratulations! You guessed the correct code.")
                break

        except ValueError as e:
            print(f"Error: {e}. Please try again.")
