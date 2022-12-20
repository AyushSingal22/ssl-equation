#!/usr/bin/env python3.7
from mpi4py import MPI
from scipy import integrate
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random
from datetime import datetime

def get_time():
    dt_obj = datetime.now()
    print('current datetime MPI :',dt_obj)
def f(t,r):
    x , y =r
    fx_t = np.cos(y)
    fy_t = np.sin(x)
    return np.array([fx_t , fy_t])

# def f2(t,r):
#     C = r
#     ep = 1.0
#     dc_dt = -C/ep
#     return dc_dt

def solve_inte(y_0):
    sol = integrate.solve_ivp(f,np.array([0,10]) , y_0, t_eval = np.linspace(0,10,100) )
    x , y = sol.y
    time = sol.t
    
    #plt.show()





if __name__=="__main__":
    
    comm = MPI.COMM_WORLD
    
    rank = comm.Get_rank()
    size = comm.Get_size()
    if rank == 0:
        
        get_time()
        for i in range(1,500):
            solve_inte(np.array([random.randint(1,10) , random.randint(1,10)]))
    elif rank == size-1:
        for i in range(1,500):
            solve_inte(np.array([random.randint(1,10) , random.randint(1,10)]))
        get_time()
    elif rank == 1:
        for i in range(1,500):
            solve_inte(np.array([random.randint(1,10) , random.randint(1,10)]))
    elif rank == 2:
        for i in range(1,500):
            solve_inte(np.array([random.randint(1,10) , random.randint(1,10)]))
    elif rank == 3:
        for i in range(1,500):
            solve_inte(np.array([random.randint(1,10) , random.randint(1,10)]))
    elif rank == 4:
        for i in range(1,500):
            solve_inte(np.array([random.randint(1,10) , random.randint(1,10)]))
    
    

    
            
    

            
        
   

        


    


    




