from maze import *
import csv
import time

N=50
M=50

data_path=[[] for i in range(100)]
data_node=[[] for i in range(100)]
data_time=[[] for i in range(100)]

maze=Maze(N,M,(0,0),(49,49))
for n in range(40):
    maze.generate()
    start_time=time.time()
    maze.Greedy()
    end_time=time.time()
    data_path[n].append(len(maze.solution))
    data_time[n].append(round((end_time-start_time)*1000))
    data_node[n].append(len(maze.explore))

    start_time=time.time()
    maze.Astar()
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
for n in range(40,80):
    maze.generate()
    start_time=time.time()
    maze.Greedy()
    end_time=time.time()
    data_path[n].append(len(maze.solution))
    data_time[n].append(round((end_time-start_time)*1000))
    data_node[n].append(len(maze.explore))

    start_time=time.time()
    maze.Astar()
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
for n in range(80,100):
    maze.generate()
    start_time=time.time()
    maze.Greedy()
    end_time=time.time()
    data_path[n].append(len(maze.solution))
    data_time[n].append(round((end_time-start_time)*1000))
    data_node[n].append(len(maze.explore))

    start_time=time.time()
    maze.Astar()
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


sdata=["Greedy","Astar","BFS","DFS"]
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