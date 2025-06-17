from maze import *
import csv
import time

# Giữ kích thước mê cung 50x50
N=50
M=50

# Giảm số lượng thử nghiệm xuống 30 bản ghi
data_path=[[] for i in range(30)]
data_node=[[] for i in range(30)]
data_time=[[] for i in range(30)]

maze=Maze(N,M,(0,0),(49,49))
for n in range(10):  
    maze.generate()

    start_time=time.time()
    maze.Astar()
    end_time=time.time()
    data_path[n].append(len(maze.solution))
    data_time[n].append(round((end_time-start_time)*1000))
    data_node[n].append(len(maze.explore))

    start_time=time.time()
    maze.Greedy()
    end_time=time.time()
    data_path[n].append(len(maze.solution))
    data_time[n].append(round((end_time-start_time)*1000))
    data_node[n].append(len(maze.explore))

    start_time=time.time()
    maze.BFS()
    end_time=time.time()
    data_path[n].append(len(maze.solution))
    data_time[n].append(round((end_time-start_time)*1000))
    data_node[n].append(len(maze.explore))

    start_time=time.time()
    maze.DFS()
    end_time=time.time()
    data_path[n].append(len(maze.solution))
    data_time[n].append(round((end_time-start_time)*1000))
    data_node[n].append(len(maze.explore))

maze=Maze(N,M,(49,49),(0,0))
for n in range(10,20):  # Điều chỉnh phạm vi vòng lặp
    maze.generate()

    start_time=time.time()
    maze.Astar()
    end_time=time.time()
    data_path[n].append(len(maze.solution))
    data_time[n].append(round((end_time-start_time)*1000))
    data_node[n].append(len(maze.explore))

    start_time=time.time()
    maze.Greedy()
    end_time=time.time()
    data_path[n].append(len(maze.solution))
    data_time[n].append(round((end_time-start_time)*1000))
    data_node[n].append(len(maze.explore))

    start_time=time.time()
    maze.BFS()
    end_time=time.time()
    data_path[n].append(len(maze.solution))
    data_time[n].append(round((end_time-start_time)*1000))
    data_node[n].append(len(maze.explore))

    start_time=time.time()
    maze.DFS()
    end_time=time.time()
    data_path[n].append(len(maze.solution))
    data_time[n].append(round((end_time-start_time)*1000))
    data_node[n].append(len(maze.explore))

maze=Maze(N,M,(10,24),(40,24))
for n in range(20,30):  # Điều chỉnh phạm vi vòng lặp
    maze.generate()

    start_time=time.time()
    maze.Astar()
    end_time=time.time()
    data_path[n].append(len(maze.solution))
    data_time[n].append(round((end_time-start_time)*1000))
    data_node[n].append(len(maze.explore))

    start_time=time.time()
    maze.Greedy()
    end_time=time.time()
    data_path[n].append(len(maze.solution))
    data_time[n].append(round((end_time-start_time)*1000))
    data_node[n].append(len(maze.explore))

    start_time=time.time()
    maze.BFS()
    end_time=time.time()
    data_path[n].append(len(maze.solution))
    data_time[n].append(round((end_time-start_time)*1000))
    data_node[n].append(len(maze.explore))

    start_time=time.time()
    maze.DFS()
    end_time=time.time()
    data_path[n].append(len(maze.solution))
    data_time[n].append(round((end_time-start_time)*1000))
    data_node[n].append(len(maze.explore))


sdata=["Astar","Greedy","BFS","DFS"]
with open('path.csv','w') as file:
    writer=csv.writer(file)
    writer.writerow(sdata)
    writer.writerows(data_path)
with open('node.csv','w') as file:
    writer=csv.writer(file)
    writer.writerow(sdata)
    writer.writerows(data_node)
with open('time.csv','w') as file:
    writer=csv.writer(file)
    writer.writerow(sdata)
    writer.writerows(data_time)

