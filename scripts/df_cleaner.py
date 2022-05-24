import numpy as np 
import pandas as pd 

def convert_to_string(df,columns):
    for col in columns:
        df[col] = df[col].astype("string")


def convert_to_numeric(df,columns):
    for col in columns:
        df[col] = pd.to_numeric(df[col])

def convert_to_int(df,columns):
    for col in columns:
        df[col]=df[col].astype("int64")

def convert_to_datetime(df,columns):
    for col in columns:
        df[col] = pd.to_datetime(df[col]) 

def multiply_by_factor(df,columns,factor):
    for col in columns:
        df[col] = df[col]*factor

def show_cols_mixed_dtypes(df):
    mixed_dtypes = {'Column': [], 'Data type': []}
    for col in df.columns:
        dtype = pd.api.types.infer_dtype(df[col])
        if dtype.startswith("mixed"):
            mixed_dtypes['Column'].append(col)
            mixed_dtypes['Data type'].append(dtype)
    if len(mixed_dtypes['Column']) == 0:
        print('None of the columns contain mixed types.')
    else:
        print(pd.DataFrame(mixed_dtypes))

def percent_missing_values(df):
    
    #calculate the total number of cells in dataframe
    totalCells = np.product(df.shape)

    #count number of missing values per column
    missingCount = df.isnull().sum()

    #calculate the total number of missing value
    totalMissing = missingCount.sum()

    #calculate the percentage of missing value
    print("The dataset contains", round(((totalMissing/totalCells) * 100), 2), "%", "missing values.")

  
    

            

