# BFS Algorithm Visualization

## Description
This Python code is designed to create a simple algorithm visualization using the Pygame library. The editor allows you to create a grid-based map by specifying the size of the grid and placing various elements, such as the starting point (Begin), the ending point (End), walls, or erasing grid cells. It also provides a feature to visualize a path on the grid using the Breadth-First Search (BFS) algorithm. 

## Prerequisites
To run this code, you need to have Python and Pygame installed on your system. You can install Pygame using pip:
```
pip install pygame
```

## Usage
1. Run the script in a Python environment.
2. The application window opens, and you can interact with it using your mouse and keyboard.

## Main Components

### Constants
- `width, height`: The dimensions of the application window.
- `win`: Pygame display object representing the window.
- `black_bg, black_sc`: Background and secondary color constants.
- `white, green, yellow, red, green1, purple`: Color constants for grid and elements.
- `fps`: Frames per second for the game loop.
- `cubeSize`: Size of individual grid cells.
- `rows`: Number of rows in the grid.

### Functions

#### `grid()`
- Draws the grid on the application window.

#### `drawWindow()`
- Draws the entire window, including the grid.

#### `main()`
- The main function that runs the game loop and handles user interactions.

#### Event Handling
- The code handles various events, including mouse clicks, keyboard input, and window closure. It tracks the active buttons and responds to user input accordingly.

#### User Interface
- Defines several buttons for actions such as selecting the grid size, placing the start (Begin), end (End), walls, erasing, and running the BFS algorithm.
- Allows users to specify the grid size, select different elements, and visualize the BFS path.
- The "Run" button triggers the BFS algorithm and path visualization.

### Pathfinding
- The code contains a section for running the BFS algorithm to find the path between the start and end points. It visualizes the path on the grid.

### Grid Interaction
- Users can interact with the grid by clicking on cells to set the start, end, walls, or erase grid elements.

### User Interface Rendering
- The code renders and updates the user interface elements, including buttons and input fields.
> **_NOTE:_**  Only one "Begin" and one "End" point can be placed on the grid.
## Usage Instructions
1. Run the script to open the application window.
2. Use the mouse to interact with the grid:
   - Click on "Size" to specify the grid size.
   - Click on "Begin," "End," "Wall," or "Erase" buttons to select an action.
   - Click on the grid cells to apply the selected action.
   - Click "Run" to visualize the path using the BFS algorithm.
3. Press "Escape" to close the application.

## Notes
- This code is a simplified level editor and path visualization tool.
- The grid size is specified using the "Size" button, with a maximum size of 32x32.
- The "Run" button triggers the BFS algorithm to find the path from the "Begin" to the "End" points.

## Disclaimer
- This code is intended for educational purposes and may require further development and optimization for production use.
