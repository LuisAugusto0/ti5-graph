import argparse
import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime
from src.implementations.sem_base import *


import sys
import os

# Add parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.columns import *
from src.graph_plot import *
from src.entries import *
from src.implementations.sem_base import *


    
if __name__ == '__main__':
    frames = SemBase.plot_cpu_percentage()
    
    

    
    
    
    
    
