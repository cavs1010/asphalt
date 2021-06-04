#%% IMPORTS
import types
import pandas as pd
import numpy as np

#%%DATA READING AND INITIAL PREPROCESSING
 
#It returns the dataframe of interes based on the property - 'AirVoids', 'MS', 'MF', 'ITS', 'TSR'
def returnDf (propertyOfInterest):
    df = pd.read_excel('fileML.xlsx', sheet_name = propertyOfInterest, engine='openpyxl')
    df = df.set_index(propertyOfInterest + ' ID')
    df.loc[:,:'Units'] = df.loc[:,:'Units'].applymap(str)
    df.loc[:,:'Units'] = df.loc[:,:'Units'] .applymap(str.strip)
    df.replace('NS', np.nan, inplace = True)
    numericColumns = ['Aggregate absorption [%]',
                  'Apparent specific gravity',
                    0.075,
                    0.3,
                    0.6,
                    2.36,
                    4.75,
                    9.5,
                    12.5,
                    19,
                    'Plastic particle size (mm)',
                    'Mixing speed (RPM)',
                    'Mixing Temperature',
                    'Mixing Time (hours)',
                    'Plastic Addition by bitumen weight (%)',
                    ]
                    
    categoricalColumns = ['Modified asphaly Mix?',
                      'Agreggate Type',
                    'Aggregate absorption [%]',
                    'Filler used',
                    'Bitumen Type Penetration Grade',
                    'New Plastic Type',
                    'Plastic pretreatment',
                    'Plastic shape',
                    'Plastic Size',
                    'Mixing Process',
                    'Plastic melted previous to addition?',
                    'Aggregates replacement ?',
                    'Bitumen replacement?',
                    'Filler replacement',
                    'Property',
                    'Units']
    df[numericColumns] = df[numericColumns].replace('N/a', 0).astype(float)
    return df
#%%
dfAirVoids = returnDf('AirVoids')
dfMS = returnDf('AirVoids')
dfMF = returnDf('MF')
dfITS = returnDf('ITS')
dfTSR = returnDf('TSR')
#%%
dfAirVoids.describe()
# %%
