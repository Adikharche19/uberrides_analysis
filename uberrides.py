import pandas as pd
import matplotlib.pyplot as pyplot
import numpy as np
# Loading the data from csv file 
uberride = pd.read_csv('/Users/sachinkharche/uberrides_analysis/Data/uber-raw-data-apr14.csv',encoding='utf-8')
uberride.head(2)
uberride.shape
uberride.duplicated().sum()