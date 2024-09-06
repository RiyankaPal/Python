import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
from IPython.display import HTML
pd.options.display.max_columns = 30
pd.options.display.float_format = '{:.2}'.format
df = pd.read_csv('movies_complete.csv', parse_dates=['release_date'])
#print("Top 5 row of movie data set:")
#print(df.head())
#print("Information of data frame:")
#df.info()
#print(df.genres[0])
#print(df['cast'][0])
#print(df.describe())
#print(df.hist(figsize=(20, 12), bins= 100))
#print(df['budget_musd'].head(10))
#print(df['budget_musd'].value_counts(dropna=False).head(20))
#print(df['revenue_musd'].value_counts(dropna=False).head(20))
#print(df['vote_average'].value_counts(dropna=False).head(20))
#print(df.describe(include='object'))
#print(df[df['title']=='Cinderella'])
# Creating a new data frame by required column of df for 
#next step to choose best and worst movies
df_best=df[['poster_path','title','budget_musd','revenue_musd','vote_count','vote_average','popularity']].copy()
#print(df_best.head())
df_best['profit_musd']=df_best['budget_musd'].sub(df['revenue_musd'])
df_best['return']=df_best['revenue_musd'].div(df['budget_musd'])
#print(df_best)
df_best.columns=['','Title','Budget','Revenue','Votes','Average Rating','Popularity','Profit','ROI']
#print(df_best)
df_best.set_index('Title',inplace=True)
#print(df_best)
#print(df_best.iloc[0,0])
subset=df_best.iloc[:5,:2]
#print(subset)
print(HTML(subset.to_html(escape=False)))




