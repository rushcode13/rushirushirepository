import pandas as pd
data={
"exercise duration(min)":[45,60,75],
"calories burnt":[100,150,200]
}
df=pd.DataFrame(data,index=['day1','day2','day3'])
print(df)