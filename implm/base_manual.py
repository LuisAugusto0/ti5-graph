import argparse
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

import sys
import os

# Add parent directory to sys.path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.columns import *
from src.entries.csv_split import *
from src.graph.simple_plot import *
from src.entries import *
from src.pre_processing.base_csv_merge import *


intervals = [
    #Interval.from_range_string("1:21 - 3:02"),
    Interval.from_range_string("3:29 - 5:01"),
    #Interval.from_range_string("6:29 - 7:01"), INVALIDO
    Interval.from_range_string("7:33 - 9:05"),
    Interval.from_range_string("9:40 - 11:12"),
    Interval.from_range_string("11:58 - 13:30")
]


class BaseManual:
    input_csv_path = 'data/base_manual.csv'
    image_path = 'example/graph_base_manual.png'
    output_prefix = 'example/base_manual/case'
    
    _frames:list[pd.DataFrame] | None = None
    

    @staticmethod
    def get_frames(input_csv = input_csv_path, output_prefix = output_prefix):
        if BaseManual._frames is None:
            BaseManual._frames = get_cases_from_csv(
                input_csv=input_csv, 
                output_prefix=output_prefix, 
                intervals=intervals, 
                save_as_csv=True
            )
        
        return BaseManual._frames
    
    
    @staticmethod
    def get_series_mean(col: Col) -> pd.Series:
        return mean_of_dataframe_list(BaseManual.get_frames())
    

    @staticmethod
    def plot_cpu_percentage(img_path:str = image_path):
        frames = BaseManual.get_frames()
        y_series_list = get_series_from_frames(frames, Col.CPU_PERCENTAGE)
        x_series = pd.Series(range(len(y_series_list[0])))
        
        plot_multiple_std(
            y_series_list= y_series_list,
            x_series = x_series,
            labels=['caso 1', 'caso 2', 'caso 3', 'caso 4', 'caso 5'],
            output=img_path,
            x_label='Segundos',
            y_label='Cpu %',
            title='Cpu % por segundo',
            y_min=0,
            y_max=100
        )
        



    
