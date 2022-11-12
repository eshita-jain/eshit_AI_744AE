import random
from time import sleep

box = 0
empty_space = 0

class player:
    def __init__(self):
        self.step=0

    def move(self,B,N,cur_x,cur_y):
        global box

        step_size = B[cur_x][cur_y]^3

        if box == 0:
            for i in range(0, N):
                for j in range(0, N):
                    if B[i][j] == step_size:
                        box += 1

        if box == 1:
            box = 0
            return self.find_next(B,N,cur_x,cur_y)

        elif box == 2:
            self.step+=1
            if B[(cur_x+1)%N][cur_y]==0:
                return (1,0)

            if B[(cur_x+N-1)%N][cur_y]==0:
                return (-1,0)
                
            if B[cur_x][(cur_y+1)%N]==0:
                return (0,1)

            if B[cur_x][(cur_y+N-1)%N]==0:
                return (0,-1)

            return self.find_next(B,N,cur_x,cur_y) 


    def find_next(self,B,N,cur_x,cur_y):
        step_size=B[cur_x][cur_y]^3
        max_d=2*N+1
        position = {"x":cur_x,"y":cur_y}

        for i in range(N):
            for j in range(N):

                if B[i][j] == empty_space:

                    dx = min ( abs(cur_x - i) , N - abs(cur_x - i) )
                    dy = min ( abs(cur_y - j) , N - abs(cur_y - j) )
                    cur_dis = dx+dy
                    if cur_dis < max_d:
                        max_d = cur_dis
                        position["x"] = i 
                        position["y"] = j 

        
        if position["x"] > cur_x:
            if position["x"]-cur_x < N/2:
                return (1,0)
            else:
                return (-1,0)

        if position["x"] < cur_x:
            if cur_x-position["x"] < N/2:
                return (-1,0)
            else:
                return (1,0)

        if position["y"] > cur_y:
            if position["y"]-cur_y < N/2:
                return (0,1)
            else:
                return (0,-1)

        if position["y"] < cur_y:
            if cur_y-position["y"] < N/2:
                return (0,-1)
            else:
                return (0,1)

        return (0,0)
