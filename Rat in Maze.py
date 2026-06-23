from collections import deque
import numpy as np
import pandas as pd


# ================= DISPLAY =================
def print_maze(maze, current_pos=None, visited=None):
    N = maze.shape[0]

    for i in range(N):
        for j in range(N):
            if current_pos == (i, j):
                print("P", end=" ")
            elif (i, j) == (N-1, N-1):
                print("E", end=" ")
            elif visited and (i, j) in visited:
                print("*", end=" ")
            elif maze[i, j] == 0:
                print("#", end=" ")
            else:
                print(".", end=" ")
        print()
    print()


# ================= DFS =================
def dfs_solution(maze):
    N = maze.shape[0]
    visited = set()
    path = []

    def dfs(x, y):
        if not (0 <= x < N and 0 <= y < N):
            return False
        if maze[x, y] == 0 or (x, y) in visited:
            return False

        visited.add((x, y))
        path.append((x, y))

        if (x, y) == (N-1, N-1):
            return True

        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            if dfs(x + dx, y + dy):
                return True

        path.pop()
        return False

    if dfs(0, 0):
        print("\n=== DFS RESULT ===")

        # 🔹 Pandas DataFrame for steps
        df = pd.DataFrame(path, columns=["Row", "Col"])
        df.index += 1
        df.index.name = "Step"

        print(df)
        print(f"\nTotal Steps (DFS): {len(path)-1}\n")

        for step, pos in enumerate(path, 1):
            print(f"DFS Step {step}:")
            print_maze(maze, pos, set(path[:step]))
    else:
        print("No DFS solution found.")


# ================= BFS =================
def bfs_solution(maze):
    N = maze.shape[0]
    queue = deque([(0, 0)])
    visited = {(0, 0)}
    parent = {(0, 0): None}

    directions = [(0,1), (1,0), (0,-1), (-1,0)]

    while queue:
        x, y = queue.popleft()

        if (x, y) == (N-1, N-1):
            path = []
            current = (x, y)

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()

            print("\n=== BFS RESULT (Shortest Path) ===")

            # 🔹 Pandas DataFrame
            df = pd.DataFrame(path, columns=["Row", "Col"])
            df.index += 1
            df.index.name = "Step"

            print(df)
            print(f"\nTotal Steps (BFS): {len(path)-1}\n")

            for step, pos in enumerate(path, 1):
                print(f"BFS Step {step}:")
                print_maze(maze, pos, set(path[:step]))
            return

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if (0 <= nx < N and 0 <= ny < N and
                maze[nx, ny] == 1 and
                (nx, ny) not in visited):

                queue.append((nx, ny))
                visited.add((nx, ny))
                parent[(nx, ny)] = (x, y)

    print("No BFS solution found.")


# ================= MANUAL =================
def solve_maze_manual(maze):
    N = maze.shape[0]
    x, y = 0, 0
    path_taken = [(0, 0)]

    print("=== Maze Game ===")
    print("W = Up | A = Left | S = Down | D = Right | Q = Quit\n")

    while True:
        print_maze(maze, (x, y), set(path_taken))

        if (x, y) == (N-1, N-1):
            print("🎉 Destination Reached!\n")

            df = pd.DataFrame(path_taken, columns=["Row", "Col"])
            df.index += 1
            df.index.name = "Step"

            print("Your Path:")
            print(df)
            print(f"\nTotal Steps (Manual): {len(path_taken)-1}\n")

            dfs_solution(maze)
            bfs_solution(maze)
            break

        move = input("Enter move: ").lower()

        if move == 'q':
            print("Game terminated.")
            break

        nx, ny = x, y

        if move == 'w': nx -= 1
        elif move == 'a': ny -= 1
        elif move == 's': nx += 1
        elif move == 'd': ny += 1
        else:
            print("Invalid input!")
            continue

        if (0 <= nx < N and 0 <= ny < N and maze[nx, ny] == 1):
            x, y = nx, ny
            path_taken.append((x, y))
        else:
            print("Blocked or out of bounds!")


# ================= MAZE (NUMPY) =================
maze = np.array([
    [1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 1, 1, 1]
])

solve_maze_manual(maze)