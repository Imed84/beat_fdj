import pandas as pd
import logging
import utils as u

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

df = df.apply(u.fill_odds, axis=1)

df =df[['Div', 'Date', 'HomeTeam', 'AwayTeam', 'FTR', 'BH', 'BD', 'BA']]

df = df.dropna()

logging.debug(f'database : {len(df)} rows')
logging.debug(df.sample(5))