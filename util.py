import pandas as pd 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


def time_bar(df,x , color =None, type ='bar'):
    if color: 
        (df.groupby([x,color])
        .ListingKey.count().reset_index()
        .pivot(columns = color,index = x ,values = 'ListingKey').T / df[x].value_counts()
        ).T.plot(kind='bar', stacked=True)
    else :
        sb.countplot(data = df, x = x )



