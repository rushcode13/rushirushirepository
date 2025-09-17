import pandas as pd #panda help convert the list or data into a more python compatible format: data frame
import numpy as np
exam_data={'name':['Katherine','Jane','Emily','Mathew','Luke','Jhon','Katie','Dyna'],
           'score':[99,10,68.45,np.nan,88,91,np.nan,47],
           'attempts':[48,9,7,2,1,9,14,12],
           'qualify':['pass','fail','pass','pass','fail','fail','pass','pass']}
labels=['a','b','c','d','e','f','g','h']
df=pd.DataFrame(exam_data,index=labels)
print("Summary of the basic information about this data frame and its data:")
print(df.info())
print(df)