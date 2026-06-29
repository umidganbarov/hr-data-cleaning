import pandas as pd
import numpy as np
from word2number import w2n
import re
df=pd.read_csv("messy_HR_data.csv")
if True:
    df['Name']
    df['Age']
    df['Salary']
    df['Gender']
    df['Department']
    df['Position']
    df['Joining Date']
    df['Performance Score']
    df['Email']
    df['Phone Number']

#print(df['Name'].isna().sum())
df['Name']=df['Name'].apply(lambda x: str(x).lower().strip())
#print(df['Age'].isna().sum()) -- there are 160 rows missing name so put em median  and numbers are in string format
df['Age']=pd.to_numeric(df['Age'],errors="coerce")
df['Age']=df['Age'].fillna(df['Age'].median())
df['Age']=df['Age'].apply(lambda x:int(x))
#print(df['Age'].sample(45))
#print(df['Salary'])
def edit(x):
    if type(x).__name__=='str':
        x=x.lower().strip()
    if pd.isna(x):
        return -1
    try:
        return int(x)
    except :
        if x.lower().startswith("n"):
            return -1
        return w2n.word_to_num(x.lower())
df['Salary']=df['Salary'].apply(edit)
md=df['Salary'].median()
#print((df['Salary']==-1).sum()) shows how many rows are nan
df['Salary']=np.where(df['Salary']==-1,md,df['Salary'])
#print(df.info())
df['Salary']=df['Salary'].astype('int')
#print(df['Salary'].value_counts())
#print(df['Gender'].isna().sum())
df['Gender']=df['Gender'].replace({'Female':'F','Male':'M',"Other":'O'})
#print(df['Gender'].value_counts())
#print(df.info())
#print(df['Department'].isna().sum())
#print(df.info())
df['Joining Date']=pd.to_datetime(df['Joining Date'],errors='coerce',format='mixed')
#print(df['Joining Date'].value_counts())
df['Year']=df['Joining Date'].dt.year
df['Month']=df['Joining Date'].dt.month
df['Day']=df['Joining Date'].dt.day
df.drop(columns=['Joining Date'],inplace=True)
df.insert(6,'Day',df.pop('Day'))
df.insert(6,'Month',df.pop('Month'))
df.insert(6,'Year',df.pop('Year'))
#print(df['Performance Score'].isna().sum())
#print(df['Performance Score'].value_counts())
#df['Performance Score']=np.where(df['Performance Score']=='A','Excellent',np.where(df['Performance Score']=='B','Good',np.where(df['Performance Score']=='C','Medium',np.where(df['Performance Score']=='D','Unsatisfied','Poor'))))
df['Performance Score']=df['Performance Score'].replace({
    'A':"Excellent",
    'B':'Good',
    'C':'Medium',
    'D':'Bad',
    'F':'Worst'
})
#print(df['Performance Score'].value_counts())
#print(df.info())
df['Email']=df['Email'].fillna('Unknown')
#print(df['Email'].value_counts())
df['Phone Number']=df['Phone Number'].fillna('000-000-0000')
df['Phone Number']=df['Phone Number'].replace(r'[ ]',000-000-000,regex=True)
#fill spaces in phone number and make all like nums 
#5555541004 like this
df['Phone Number']=df['Phone Number'].replace(0,'000-000-0000')
print(df['Phone Number'].value_counts())
df['Phone Number']=df['Phone Number'].replace(r'[-]','',regex=True)
print(df['Phone Number'].value_counts())
print(df['Phone Number'].dtype)        # if int64, that's the problem
print(df['Phone Number'].iloc[2])  


df.to_csv("output.csv",index=False)
#! Data is cleaned :D
