import random

class Node:
    def __init__(self,state=None):
        self.state=state
        self.parent=None

    def __eq__(self, other):
        return isinstance(other, Node) and self.state==other.state

    def __hash__(self):
        return hash(("node",self.state))

    def set_parent(self,node):
        self.parent=node
    
    def get_parent(self):
        return self.parent


class Stack:
    def __init__(self):
        self.data=[]
    def push(self,node):
        self.data.append(node)
    def pop(self):    
        res=self.data.pop()
        return res
    def empty(self):
        return len(self.data)==0    
    def contain(self,node_state):
        for node in self.data:
            if node_state==node.state:
                return True
        return False

class Queue(Stack):
    def pop(self):
        res=self.data.pop(0)
        return res

class Maze:
    def __init__(self,N,M,P0,P1):
        self.path=[]
        self.wall=[]
        self.explore=[]
        self.solution=[]
        self.height=N
        self.width=M
        self.start=P0
        self.end=P1
        self.maze=[['██' for i in range(M)] for i in range(N)]

    def neighbor(self,node):
        neighbor=list()
        possible=[(node.state[0],node.state[1]-1),(node.state[0]-1,node.state[1]),(node.state[0],node.state[1]+1),(node.state[0]+1,node.state[1])]
        for i in possible:
            if 0<=i[0]<=self.height-1 and 0<=i[1]<=self.width-1:
                neighbor.append(i)
        return neighbor
    
    # Check if the position is walkable(there are at least 2 neighbors in path)
    def check(self,node):
        count=0
        for state in self.neighbor(node):
            if state in self.path:
                count+=1
        if count>=2:
            return False
        return True

    def h(self,node):
        return abs(self.end[0]-node.state[0])+abs(self.end[1]-node.state[1])

    def g(self,node):
        if node in g_score:
            pass
        else:
            g_score[node]=g_score.get(node.get_parent())+1
        return g_score[node]

    def f(self,node):
        return self.g(node)+self.h(node)

    # Generating a maze
    def generate(self):
        self.path=[]
        self.maze=[['██' for i in range(self.width)] for i in range(self.height)]
        S=Stack()
        start_node=Node(state=self.start)
        start_node.set_parent(None)
        S.push(start_node)
        while S.empty()==False:
                
            P=S.pop()
            if self.check(P):
                self.maze[P.state[0]][P.state[1]]='  '
                self.path.append(P.state)
                containP1=None
                neighbor=self.neighbor(P)
                random.shuffle(neighbor)
                for state in neighbor:
                    node=Node(state=state)
                    node.set_parent(P)
                    if state==self.end:
                        containP1=Node(state=self.end)
                        containP1.set_parent(P)
                    elif state not in self.path and not S.contain(node) and self.check(node) :
                        S.push(node)
                if containP1 is not None:
                    S.push(containP1)
            else:
                self.wall.append(P.state)

        self.make_complex()
        
        if self.end not in self.path:
            self.generate()
        
        self.maze[self.start[0]][self.start[1]]='SP'
        self.maze[self.end[0]][self.end[1]]='EP'

    # Greedy Best-first Search solver
    def Greedy(self):
        self.explore=[]
        self.solution=[]
        start_node=Node(state=self.start)
        start_node.set_parent(None)
        fringe=dict()
        fringe[start_node]=self.h(start_node)
    
        while len(fringe)!=0:
            node=min(fringe,key=fringe.get)
            fringe.pop(node)
            self.explore.append(node.state)
            if node.state==self.end:
                while node!=None:
                    self.solution.append(node.state)
                    node=node.parent
                self.solution.reverse()
                break
            else:
                for state in self.neighbor(node):
                    temp=Node(state=state)
                    if state in self.explore or state not in self.path or temp in fringe:
                        pass
                    else: 
                        fringe[temp]=self.h(temp)
                        temp.set_parent(node)

    # A* Search solver
    def Astar(self):
        global g_score
        start_node=Node(state=self.start)
        start_node.set_parent(None)
        g_score={}
        g_score[start_node]=0
        self.explore=[]
        self.solution=[]
        fringe=dict()
        fringe[start_node]=self.h(start_node)
    
        while len(fringe)!=0:
            node=min(fringe,key=fringe.get)
            fringe.pop(node)
            self.explore.append(node.state)
            if node.state==self.end:
                while node!=None:
                    self.solution.append(node.state)
                    node=node.parent
                self.solution.reverse()
                break
            else:
                for state in self.neighbor(node):
                    temp=Node(state=state)
                    if state in self.explore or state not in self.path:
                        pass
                    elif temp in fringe:
                        g_temp=g_score.get(node)+1
                        f_temp=g_temp+self.h(temp)
                        if g_temp<g_score.get(temp):
                            fringe.pop(temp)
                            fringe[temp]=f_temp
                            temp.set_parent(node)
                            g_score[temp]=g_temp

                    else: 
                        temp.set_parent(node)
                        fringe[temp]=self.f(temp)
                        g_score[temp]=g_score.get(node)+1

    # Breadth First Search solver
    def BFS(self):
        self.explore=[]
        self.solution=[]
        start_node=Node(state=self.start)
        start_node.set_parent(None)
        fringe = Queue()
        fringe.push(start_node)
        
        while not fringe.empty():
            node = fringe.pop()
            self.explore.append(node.state)
            if node.state == self.end:
                while node != None:
                    self.solution.append(node.state)
                    node=node.parent
                self.solution.reverse()
                break
            else:  
                for state in self.neighbor(node):
                    if state in self.path and state not in self.explore and not fringe.contain(state):
                        child=Node(state=state)
                        child.set_parent(node)
                        fringe.push(child)

    # Depth First Search solver
    def DFS(self):
        self.explore=[]
        self.solution=[]
        start_node=Node(state=self.start)
        start_node.set_parent(None)
        fringe = Stack()
        fringe.push(start_node)
        
        while not fringe.empty():
            node = fringe.pop()
            self.explore.append(node.state)
            if node.state == self.end:
                while node != None:
                    self.solution.append(node.state)
                    node=node.parent
                self.solution.reverse()
                break
            else:  
                for state in self.neighbor(node):
                    if state in self.path and state not in self.explore and not fringe.contain(state):
                        child=Node(state=state)
                        child.set_parent(node)
                        fringe.push(child)

    # Remove some walls to make the maze more complicated   
    def make_complex(self):
        ran_num=random.randint(0,len(self.wall)//10)
        for i in range(ran_num):
            remove=random.choice(self.wall)
            self.wall.remove(remove)
            self.path.append(remove)

    # Print the maze
    def printMaze(self):
        for x in range(self.width):
            for y in range(self.height):
                if (x,y) == self.start:
                    print("SP", end='')
                elif (x,y) == self.end:
                    print("EP", end='')
                elif (x,y) in self.solution:
                    print("**", end='')
                elif (x,y) in self.explore:
                    print("==", end='')
                else:
                    print(self.maze[x][y],end='')
            print()
