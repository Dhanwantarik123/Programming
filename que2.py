import pandas as pd
import numpy as np
exam_data = {
	'name': ['Ajay', 'Vijay', 'Vivek', 'Atharv', 'Apurva', 'Rupal', 'Priyal',
'Shrushti', 'Vishal', 'Pranay'],
	'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
	'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
	'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df=pd.DataFrame(exam_data,index=labels)
print(df[["name","score"]])
print(df[(df[score]>=15 )&( df[score]<=20)])
#print(df[(df['score'] >= 15) & (df['score'] <= 20)])
print(df[df("score".isna())])
df.loc['d','score']=11.5
print(df.loc['d'])
print(df['attempts'].sum())


