import pandas as pd 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


def time_bar(df,x , color =None, type ='bar' , ispercent = True):
    if color:
        if ispercent:
            (df.groupby([x,color])
            .count().max(axis = 1).reset_index()
            .pivot(columns = color,index = x ,values = 0).T/ df[x].value_counts()
            ).T.plot(kind='bar', stacked=True)
        else:
            (df.groupby([x,color])
            .count().max(axis = 1).reset_index()
            .pivot(columns = color,index = x ,values = 0)).plot(kind='bar', stacked=True)
    else :
        sb.countplot(data = df, x = x )



