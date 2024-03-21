import pandas as pd
import logging
import utils as u
from sklearn.model_selection import train_test_split

with open('my_log_file.log', 'w'):
    pass

logging.basicConfig(filename='my_log_file.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('START')

df = pd.DataFrame()
# parse excel file containing several sheets
for i in u.files:
    data = pd.read_excel('database/' + i, sheet_name=None)
    df_temp = pd.concat(data.values(), ignore_index=True)
    df = pd.concat([df, df_temp], ignore_index=True)

logging.debug(f'database befor odds retrieval: {len(df)} rows')

df = df.apply(u.fill_odds, axis=1, logger=logging)
df =df[['Div', 'Date', 'HomeTeam', 'AwayTeam', 'BH', 'BD', 'BA', 'FTR']]
df = df.dropna()

logging.debug(f'database : {len(df)} rows')
logging.debug(df.sample(5))

X = df[['BH', 'BD', 'BA']]
Y = df['FTR']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
