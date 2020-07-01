import pandas as pd
pd.set_option('display.max_colwidth', -1)

df = pd.read_csv('jeopardy.csv')
print(df.head())
#print(df.columns)
df.columns = ['Show_Number', 'Air_Date', 'Round', 'Category', 'Value','Question', 'Answer']
print(df.columns)
