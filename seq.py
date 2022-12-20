#!/usr/bin/env python3.7
from mpi4py import MPI
from scipy import integrate

import pandas as pd
import numpy as np
import random
from datetime import datetime

def get_time():
    dt_obj = datetime.now()
    print('current datetime SEQ :',dt_obj)
def f(t,r):
    x , y =r
    fx_t = np.cos(y)
    fy_t = np.sin(x)
    return np.array([fx_t , fy_t])
def solve_inte(y_0):
    sol = integrate.solve_ivp(f,np.array([0,10]) , y_0, t_eval = np.linspace(0,10,100) )
    x , y = sol.y
    time = sol.t
   
if __name__=="__main__":
    get_time()
    for i in range( 0,3000):
        solve_inte(np.array([random.randint(1,10) , random.randint(1,10)]))
    
    get_time()