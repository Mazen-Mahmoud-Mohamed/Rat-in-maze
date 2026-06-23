# 🐭 Rat in a Maze Solver

An interactive Python implementation of the classic **Rat in a Maze** problem using:

- Depth First Search (DFS)
- Breadth First Search (BFS)
- Manual Player Navigation
- NumPy Maze Representation
- Pandas Step Tracking

The project allows users to manually solve the maze and then compare their solution against DFS and BFS algorithms.

---

# ✨ Features

## 🎮 Interactive Maze Game
- Move through the maze manually
- WASD controls
- Real-time maze visualization
- Track visited cells

## 🔍 DFS Solver
- Recursive Depth First Search
- Finds a valid path to the destination
- Displays step-by-step traversal
- Shows total path length

## 🚀 BFS Solver
- Breadth First Search implementation
- Finds the shortest path
- Reconstructs solution using parent tracking
- Displays optimal route

## 📊 Data Analysis
- Uses Pandas DataFrames
- Records every move
- Displays path coordinates
- Tracks step count

## 🧩 Maze Visualization
Symbols:

| Symbol | Meaning |
|----------|----------|
| P | Current Position |
| E | Exit |
| * | Visited Cell |
| . | Walkable Path |
| # | Blocked Cell |

---

# 🛠 Technologies Used

- Python
- NumPy
- Pandas
- Collections (deque)

---

# 📦 Installation

Install dependencies:

```bash
pip install numpy pandas
```

---

# ▶ Usage

Run:

```bash
python "Rat in Maze.py"
```

Controls:

```text
W = Move Up
A = Move Left
S = Move Down
D = Move Right
Q = Quit
```

---

# 🗺 Maze Layout

Default Maze:

```text
. # # # #
. . # # #
# . . . #
# # # . #
. . . . E
```

---

# 🧠 Algorithms

## DFS (Depth First Search)

Characteristics:

- Explores as deep as possible first
- Recursive implementation
- May not find the shortest path
- Fast and memory efficient

### Time Complexity

```text
O(V + E)
```

---

## BFS (Breadth First Search)

Characteristics:

- Explores level by level
- Guarantees shortest path
- Uses a queue
- Ideal for shortest-route problems

### Time Complexity

```text
O(V + E)
```

---

# 📈 Example Output

```text
=== BFS RESULT (Shortest Path) ===

Step | Row | Col
----------------
1    | 0   | 0
2    | 1   | 0
3    | 1   | 1
...
```

The program also visualizes every step of the solution.

---

# 📂 Project Structure

```text
project/
│
├── Rat in Maze.py
└── README.md
```

---

# 🎯 Learning Objectives

This project demonstrates:

- Graph traversal algorithms
- DFS recursion
- BFS shortest path search
- Queue data structures
- Matrix navigation
- Path reconstruction
- Game-like terminal interaction

---

# 🔮 Future Improvements

- GUI Version
- Random Maze Generator
- A* Pathfinding
- Dijkstra Algorithm
- Maze Import/Export
- Colored Terminal Output
- Animated Visualization
- Difficulty Levels

---

# 🎓 Educational Value

Perfect for learning:

- Artificial Intelligence fundamentals
- Pathfinding algorithms
- Graph theory
- Data structures
- Problem-solving techniques

---

# ⭐ Support

If you found this project useful:

- Star the repository
- Fork the project
- Improve the algorithms
- Add new maze types

---

Made with ❤️ using Python, DFS, BFS, NumPy, and Pandas.
