import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("MS_Dhoni_ODI_record.csv")

print(df.head())
print(df.tail())

print(df['opposition'])
df['opposition']=df['opposition'].apply(lambda x: x[2:])
print(df['opposition'])


df['date']=pd.to_datetime(df['date'],dayfirst=True)
df['year']=df['date'].dt.year.astype(int)
print(df.year)
print(df['year'])

df['score']=df['score'].apply(str)
df['not_out']=np.where(df['score'].str.endswith('*'),1,0)
print(df.not_out)


df.drop(columns='odi_number', inplace=True)




df_new = df.loc[((df['score'] != 'DNB') & (df['score'] != 'TDNB')),'runs_scored' : ]

# fixing the data types of numerical columns
df_new['runs_scored'] = df_new['runs_scored'].astype(int)
df_new['balls_faced'] = df_new['balls_faced'].astype(int)
df_new['strike_rate'] = df_new['strike_rate'].astype(float)
df_new['fours'] = df_new['fours'].astype(int)
df_new['sixes'] = df_new['sixes'].astype(int)

# Career stats
first_match_date = df['date'].dt.date.min().strftime('%B %d, %Y') # first match
print('First match:', first_match_date)
last_match_date = df['date'].dt.date.max().strftime('%B %d, %Y') # last match
print('Last match:', last_match_date)
number_of_matches = df.shape[0] # number of mathces played in career
print('Number of matches played:', number_of_matches)
number_of_inns = df_new.shape[0] # number of innings
print('Number of innings played:', number_of_inns)
not_outs = df_new['not_out'].sum() # number of not outs in career
print('Not outs:', not_outs)
runs_scored = df_new['runs_scored'].sum() # runs scored in career
print('Runs scored in career:', runs_scored)
balls_faced = df_new['balls_faced'].sum() # balls faced in career
print('Balls faced in career:', balls_faced)
career_sr = (runs_scored / balls_faced)*100 # career strike rate
print('Career strike rate: {:.2f}'.format(career_sr))
career_avg = (runs_scored / (number_of_inns - not_outs)) # career average
print('Career average: {:.2f}'.format(career_avg))
highest_score_date = df_new.loc[df_new.runs_scored == df_new.runs_scored.max(), 'date'].values[0]
highest_score = df.loc[df.date == highest_score_date, 'score'].values[0] # highest score
print('Highest score in career:', highest_score)
hundreds = df_new.loc[df_new['runs_scored'] >= 100].shape[0] # number of 100s
print('Number of 100s:', hundreds)
fifties = df_new.loc[(df_new['runs_scored']>=50)&(df_new['runs_scored']<100)].shape[0] #number of 50s
print('Number of 50s:', fifties)
fours = df_new['fours'].sum() # number of fours in career
print('Number of 4s:', fours)
sixes = df_new['sixes'].sum() # number of sixes in career
print('Number of 6s:', sixes)


df['opposition'].value_counts().plot(kind='bar',title='Number of matches against different oppositions',figsize=(8,5))
plt.show()

runs_scored_by_opposition=pd.DataFrame(df_new.groupby('opposition')['runs_scored'].sum())
runs_scored_by_opposition.plot(kind='bar',title='Runs scored against different oppositions',figsize=(8,5))
plt.xlabel(None);
plt.show()


#Year-wise record
df['year'].value_counts().sort_index().plot(kind='bar',title='Matches played by year',figsize=(8,5))
plt.xticks(rotation=0)
plt.show()