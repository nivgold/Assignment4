import pandas as pd
import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt
import statistics as stats
from tkinter import messagebox
from sklearn import preprocessing
from tkinter import *

def pre_process(path):
    try:
        df = pd.read_excel(path)
        # filling missing values with mean value in the column
        df = df.fillna(df.mean())

        # standartidation
        df_no_country = df.drop(['country'], axis=1)
        scaler = preprocessing.StandardScaler()
        scaled_df = scaler.fit_transform(df_no_country)
        df_no_country = pd.DataFrame(scaled_df, columns=df_no_country.columns)
        df = pd.concat([pd.DataFrame(df["country"]), df_no_country], axis=1)

        # kibutz data
        df = df.groupby(['country'], as_index=False).mean()
        df = df.drop(['year'], axis=1)
        return df

    except FileNotFoundError as e:
        raise Exception("Please enter a database path")
    except Exception as e:
        raise Exception("The entered path isn't fit. Please enter new path")
