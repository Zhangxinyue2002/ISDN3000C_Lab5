import pandas as pd
import numpy as np

time_range = pd.to_datetime(pd.date_range(start='2023-07-01', end='2023-07-31', freq='H'))
print(time_range)
