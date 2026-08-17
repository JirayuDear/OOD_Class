# Data Structures & Object-Oriented Design (OOD) - Python Laboratory Repository

A comprehensive collection of Python implementations covering fundamental to advanced **Data Structures and Algorithms (DSA)** along with **Object-Oriented Design (OOD)** principles. This repository contains structured laboratory exercises, real-world scenario modeling, algorithm implementations, and exam preparation code.

---

## 🛠 Tech Stack

- **Primary Language:** Python 3.8+
- **Paradigm:** Object-Oriented Programming (OOP) & Imperative Programming
- **Libraries/Dependencies:** Python Standard Library (`sys`, `math`, `typing`, etc.)

---

## 🌟 Key Features & Module Overview

The repository is organized by modular topics ranging from basic Python syntax and class implementations to complex graph algorithms:

### 1. Basic Algorithms & Object-Oriented Design (`Lab_01` - `Lab_02`)
- **Mathematical & String Manipulation:** Vickrey second-price auction logic, pattern drawing with nested loops, string highlighting, and base-conversion puzzles.
- **OOP Implementations:** 
  - Operator overloading (`+`, `-`, `*`, `/`) in arithmetic classes.
  - State-driven string chaining games (*TorKham* / Word Chain).
  - Geometric modeling (Spheres, volume/surface area calculation with internal state management).

### 2. Linear Data Structures (`Lab_03` - `Lab_05`)
- **Stacks (`Lab_03`):** 
  - Monotonic stack implementations for the *Next Greater Element* problem.
  - Base conversion (Decimal to Binary).
  - Physical simulation: Gym barbell plate balancing and dynamic loading optimization.
  - Game combat resolution using HP-based stack state.
- **Queues (`Lab_04`):**
  - Multi-queue scheduling and simulation (Cashier/Checkout queues with varying service rates).
  - Hot Potato (Josephus-style elimination) simulation.
  - Nested Queue of Queues with category grouping.
  - Event-driven Printer spooling engine with integrated Stack (tray) and Queue (buffer).
- **Linked Lists (`Lab_05`):**
  - Singly Linked List with head/tail pointers and arbitrary node insertions/deletions.
  - In-place node manipulation: Bubble Sort via pointer manipulation.
  - Dynamic group reversal ($k$-group node reversal).
  - Directed Graph / Git branch intersection and merge-base detection via linked structures.

### 3. Recursion & Divide-and-Conquer (`Lab_06`)
- Recursive Min-finding and recursive sorting.
- Power set / Subsequence generation using backtracking.
- 2D Grid Flood-Fill algorithm (*Water Flow* simulation).
- Recursive mineral purification weight calculation based on Fibonacci thresholds.

### 4. Tree Data Structures (`Lab_07` - `Lab_08`)
- **Binary Search Trees (BST - `Lab_07`):**
  - Insertion, deletion, and in-order / level-order tree traversals.
  - Root-to-leaf path summation checks and tree transformations.
  - Pathfinding: Treasure hunt and escape route tracking.
  - Depth-specific Tree Mirroring.
- **Self-Balancing Trees (AVL Trees - `Lab_08`):**
  - Height calculation, balance factor monitoring, and single/double rotations (`LL`, `RR`, `LR`, `RL`).
  - Order-statistic queries ($k$-th smallest element search).
  - Structural validation (`isBST`, `isAVL`).
  - Concrete application: *RottenPotato* movie rating indexing engine with range search and top-N ranking.

### 5. Sorting & Searching Algorithms (`Lab_09` - `Lab_10`)
- **Sorting (`Lab_09`):** 
  - Bubble Sort (with step-by-step movement visualization).
  - Insertion Sort (recursive and iterative).
  - Custom multi-key comparison (Frequency sorting, Alphabetical character extraction, Football league table points/goal-difference evaluation).
- **Searching & Hashing (`Lab_10`):**
  - Fractional Binary Search for exact percentile calculations.
  - Self-Organizing Lists (Move-To-Front heuristic for book caching).
  - Hash Tables with Open Addressing (Quadratic Probing collision handling).
  - Dynamic Rehashing with load-factor threshold checks and prime table sizing.
  - Binary Search over Solution Space: Box packing weight capacity optimization.

### 6. Graph Theory & Algorithms (`Lab_11`)
- Adjacency Matrix and Adjacency List construction.
- Depth-First Search (DFS) and Breadth-First Search (BFS) for connected and disconnected components.
- **Shortest Path Algorithms:**
  - Dijkstra’s Algorithm for single-source shortest path on weighted graphs.
  - Unweighted Shortest Path on the London Underground network (Tubemap) using BFS path reconstruction.

---

## 📂 Project Structure

```plaintext
.
├── Lab_01/                 # Fundamentals & Problem Solving
│   ├── Lab_01_01.py        # Rabbit & Turtle speed/distance problem
│   ├── Lab_01_02.py        # Conditionals & product vs sum logic
│   ├── Lab_01_03.py        # Character highlighting
│   ├── Lab_01_04.py        # Geometric pattern generation
│   └── Lab_01_05.py        # Vickrey Auction engine
├── Lab_02/                 # Object-Oriented Programming
│   ├── Lab_02_01.py        # Calculator class with operator overloading
│   ├── Lab_02_02.py        # Spherical geometric model
│   ├── Lab_02_03.py        # TorKham HanSaa (Word Chain Game)
│   ├── Lab_02_04.py        # Base-N Age converter
│   └── Lab_02_05.py        # Secret Code / Letter index cipher
├── Lab_03/                 # Stacks
│   ├── Lab_03_01.py        # Stack push constraints (Difference of 5/10)
│   ├── Lab_03_02.py        # Gym Barbell Plate Loading Simulator
│   ├── Lab_03_03.py        # RPG Battle / HP Damage Stack resolution
│   ├── Lab_03_04.py        # Monotonic Stack (Next Greater Element)
│   └── Lab_03_05.py        # Decimal to Binary conversion
├── Lab_04/                 # Queues
│   ├── Lab_04_01.py        # Basic Queue operations
│   ├── Lab_04_02.py        # Multi-Counter Queue simulation
│   ├── Lab_04_03.py        # Hot Potato game simulation
│   ├── Lab_04_04.py        # Nested Queue grouping system
│   └── Lab_04_05.py        # Event-driven Print Spooler (Queue + Stack)
├── Lab_05/                 # Linked Lists
│   ├── Lab_05_01.py        # Locomotive train rearrangement
│   ├── Lab_05_02.py        # Singly Linked List Bubble Sort
│   ├── Lab_05_03.py        # Git history & merge point detection
│   ├── Lab_05_04.py        # Ant Colony queue management
│   └── Lab_05_05.py        # K-Group Linked List Reversal
├── Lab_06/                 # Recursion & Backtracking
│   ├── Lab_06_01.py        # Recursive minimum element
│   ├── Lab_06_02.py        # Recursive Bubble Sort
│   ├── Lab_06_03.py        # Subsets / Combinations generation
│   ├── Lab_06_04.py        # 2D Grid Water Flow Flood-Fill
│   └── Lab_06_05.py        # Recursive Mineral Purification
├── Lab_07/                 # Binary Search Trees (BST)
│   ├── Lab_07_01.py        # BST Construction and 2D Visualization
│   ├── Lab_07_02.py        # Target Path Sum validation
│   ├── Lab_07_03.py        # BST Node Value Scaling and Summation
│   ├── Lab_07_04.py        # Treasure Hunt / Maze pathfinding
│   └── Lab_07_05.py        # Level-Order insertion and Mirroring
├── Lab_08/                 # Balanced Trees (AVL Trees)
│   ├── Lab_08_01.py        # AVL Tree with K-th smallest query
│   ├── Lab_08_02.py        # Tree comparison and structural equality
│   ├── Lab_08_03.py        # Maximum path sum tracking
│   ├── Lab_08_04.py        # BST vs AVL Balance verification
│   └── Lab_08_05.py        # RottenPotato Movie Catalog AVL implementation
├── Lab_09/                 # Sorting Algorithms
│   ├── Lab_09_01.py        # Bubble sort step tracing
│   ├── Lab_09_02.py        # Element frequency sort
│   ├── Lab_09_03.py        # Recursive Insertion Sort
│   ├── Lab_09_04.py        # Character extraction sorting
│   └── Lab_09_05.py        # Sports League Table ranking
├── Lab_10/                 # Searching & Hashing
│   ├── Lab_10_01.py        # Interpolated Binary Search Percentile
│   ├── Lab_10_02.py        # Move-To-Front Self-Organizing Cache
│   ├── Lab_10_03.py        # Hash Table with Quadratic Probing
│   ├── Lab_10_04.py        # Dynamic Rehashing & Threshold Scaling
│   └── Lab_10_05.py        # Capacity allocation via Binary Search on answer
├── Lab_11/                 # Graph Algorithms
│   ├── Lab_11_01.py        # Adjacency Matrix Builder
│   ├── Lab_11_02.py        # Graph Traversals (Full DFS & BFS)
│   ├── Lab_11_03.py        # All-Pairs / Query-based Shortest Path
│   ├── Lab_11_04.py        # London Tube Map Shortest Route (BFS)
│   └── Lab_11_05.py        # Dijkstra's Algorithm implementation
└── pratice_Exam/           # Additional Exam Review & Classic Implementations
    ├── sort_pratice/       # Bubble, Insertion, Selection, Shell sorts
    ├── implement_avl.py    # Standalone clean AVL Tree implementation
    ├── implement_bst.py    # Standalone clean BST implementation
    └── pratice_tree_*.py   # Tree traversal and manipulation variants
```

---

## 🚀 How to Run

### Prerequisites
- Python 3.8 or higher installed on your machine.

### Execution
Run any script directly using the standard Python interpreter. Most scripts parse standard console input (`stdin`).

```bash
# Example 1: Run Gym Barbell Stack Simulation
python Lab_03/Lab_03_02.py

# Example 2: Run Movie AVL Tree System
python Lab_08/Lab_08_05.py

# Example 3: Run Dijkstra Shortest Path
python Lab_11/Lab_11_05.py
```

### Sample Input Formats
Many modules expect delimited input formats:
- **Comma/Slash separated numbers:** `1,2,3/10`
- **Graph queries:** `A 1 B, B 2 C / A C`
- **Space-separated inputs:** `10 20 30 40 50`

---

## 💡 Code Highlights

- **Pure Python Data Structures:** Custom node-based implementations of Stacks, Queues, Linked Lists, BSTs, AVL Trees, and Hash Tables without third-party libraries.
- **Tree Visualization:** Built-in console visualizers (`printTree`, `printTreeVisual`) to easily debug tree balances, heights, and rotations.
- **Algorithmic Correctness:** Clean implementations of rotations (LL, RR, LR, RL), graph search, and monotonic data structures.