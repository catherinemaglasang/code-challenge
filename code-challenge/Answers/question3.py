'''
    Question 3 (Python):

    Given Table 4; 
    what is the python syntax to transform a (input) dataframe to an (output) dataframe 
    with createdDTS  and t3id as the index, columns from metric, and column values from value? 
'''

import numpy as np
import pandas as pd

# import dataframe from csv
df = pd.read_csv('../Data/table4.csv')  

# transform imported datafame into the desired output
df_transformed = df.set_index(['t3id', 'createdDTS', 'metric'])['value'].unstack()

print('\nINPUT DATAFRAME\n\n', df)
print('\n----------------------------------------')
print('\nOUTPUT DATAFRAME\n\n', df_transformed)