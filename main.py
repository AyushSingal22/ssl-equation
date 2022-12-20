import os
os.system("mpiexec -n 6 python -m mpi4py mpi.py")
os.system("py seq.py")