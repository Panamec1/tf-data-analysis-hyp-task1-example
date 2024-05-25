import pandas as pd
import numpy as np
from scipy.stats import shapiro


chat_id = 905420197 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    alpha = 0.08
    t = x_cnt/x_success - y_cnt/y_success

    if t > alpha:
        return True
    else:
        return False

