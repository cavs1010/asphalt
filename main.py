#%% IMPORTS
import pandas as pd
import numpy as np

#%% Data Reading and initial pre-processing
df = pd.read_excel('fileML.xlsx', sheet_name = 'AirVoids', engine='openpyxl')
df = df.set_index('Air Voids ID')
df = df.applymap(str)
#df.columns = df.columns.str.strip()
df = df.applymap(str.strip)


#%% 

