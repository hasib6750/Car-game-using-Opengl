
# Car Game - OpenGL Python

This is a simple car-avoidance game built using Python and the `PyOpenGL` library. The game simulates a car driving on a road where the player must avoid falling obstacles. The difficulty increases as the game progresses, with the speed of the obstacles gradually increasing. The game ends if the car collides with any obstacle.

## Features
- **Car Movement**: The player can move the car left or right using the 'A' and 'D' keys.
- **Obstacles**: The game features two types of obstacles:
  - **Round Objects**: These obstacles fall from the top and their size increases as they approach the bottom.
  - **Square Objects**: These obstacles fall in a square shape and rotate while descending.
- **Collision Detection**: The game detects collisions between the car and the falling obstacles. The game ends if the car collides with a round object.
- **Score System**: The score increases continuously as the game progresses, with bonus points added when the car hits square objects.
- **Increasing Difficulty**: As the game goes on, the speed of the obstacles increases, making the game more challenging.
- **Game Over Screen**: When the player crashes, a game over message appears, and the score is displayed.

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/car-avoidance-game.git
   ```

2. Navigate to the project directory:
   ```
   cd car-avoidance-game
   ```

3. Install the required dependencies:
   ```
   pip install PyOpenGL
   ```

## How to Play

1. Run the game using:
   ```
   python game.py
   ```

2. Use the 'A' key to move the car left and the 'D' key to move it right.

3. Avoid the falling obstacles and try to achieve the highest score possible.

4. If the car collides with a round object, the game ends and the score is displayed.

## Technologies Used
- **Python**: The programming language used for the game.
- **PyOpenGL**: The OpenGL wrapper for Python used for rendering the game in 2D.

## Contributing

Feel free to fork this repository and submit pull requests for improvements, bug fixes, or new features!

## License

This project is open-source and available under the [MIT License](LICENSE).
