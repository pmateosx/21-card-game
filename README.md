# Fun Card Game

This project is a simple and fun command-line card game.

## About the Game

This is an interactive card game where the goal is to get a hand total as close to 21 as possible without going over. You play against a dealer.

-   **Cards:** Standard playing cards are used. Number cards are worth their face value, face cards (J, Q, K) are worth 10, and Aces can be 1 or 11.
-   **Gameplay:**
    -   You and the dealer are each dealt two cards.
    -   You can choose to 'hit' (take another card) or 'stand' (keep your current hand).
    -   If your hand exceeds 21, you 'bust' and lose.
    -   Once you stand, the dealer plays their hand, typically hitting until their score is 17 or more.
    -   The winner is the one closest to 21 without busting.

## How to Run

### Standard Execution

1.  Ensure you have Python 3 installed on your system.
2.  Open your terminal or command prompt.
3.  Navigate to the directory where `main.py` is located.
4.  Run the game using the following command:
    ```bash
    python main.py
    ```
5.  Follow the on-screen prompts to play the game. Enter 'y' to get another card or 'n' to stand.

### Using Dev Containers (Recommended)

If you have Docker and VS Code installed, you can use the provided Dev Container configuration for a consistent development environment.

1.  Open this project in VS Code.
2.  If prompted to "Reopen in Container", click it. Otherwise, open the Command Palette (Ctrl+Shift+P or Cmd+Shift+P) and select "Dev Containers: Reopen in Container".
3.  Once the container is built and started, open a new terminal in VS Code.
4.  Navigate to the project directory (it should open there by default).
5.  Run the game using the same command:
    ```bash
    python main.py
    ```

Enjoy the game!
