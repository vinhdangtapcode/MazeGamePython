# SOLVING MAZE BASED ON HEURISTIC SEARCH (A* SEARCH)

## Description

* **Initial State**: Normally we will let the starting point have coordinates (0,0) and the destination point with coordinates (M,N). We expand the problem that the initial state can be created with P0 and P1 at any coordinates on the path of the maze.
* **Action**: From the current coordinates we can go left, right, up or down if not blocked by the wall of the maze and we cannot go diagonally.
* **Goal Test**:  We reach the destination.
* **Path Cost**: Each step costs 1 and the cost is uniform.


## Getting Started

### Dependencies
* Python
* pygame library

### Installing
1. Download this project as zip and extract it.
2. Install **pygame** .

    * Windows installation
    ```
    py -m pip install -U pygame --user
    ```

    * Mac installation
    ```
    python3 -m pip install -U pygame --user
    ```

### Executing program

* **maze.py** consists of all data structures and algorithms using in this project.
* **maze_game.py** creates a pygame window showing a random maze and solutions with respect to each algorithms.
* **Astar_running.py** creates a pygame window displaying the progress of generating a maze and solving it by A*.
* **test.py** is the file to solve this problem for 100 different instances with size 50x50 and write the _number of explored nodes_, _running time(ms)_, _length of solution_ into 3 .csv file **node.csv**, **time.csv**, **path.csv**, repectively. 
* **node_report.csv**, **time_report.csv**, **path_report.csv** are files that we use to analyse and make comparision in our report.

## Contributors
* Trịnh Hoàng Giang: giang.th214893@sis.hust.edu.vn
* Hoàng Thành Đạt: dat.ht214889@sis.hust.edu.vn
* Lăng Văn Quý: quy.lv214928@sis.hust.edu.vn
* Hồ Ngọc Ánh: anh.hn214877@sis.hust.edu.vn
