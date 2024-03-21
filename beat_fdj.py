import pandas as pd
import logging
import utils as u
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import matplotlib.pyplot as plt

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
#get month number from date
df['Month'] = pd.DatetimeIndex(df['Date']).month

scaler = MinMaxScaler()
df['Month_scaled'] = scaler.fit_transform(df[['Month']])

logging.debug(f'database : {len(df)} rows')
logging.debug(df.sample(5))

# machine learning
X = df[['BH', 'BD', 'BA', 'Month_scaled']]
Y = pd.get_dummies(df['FTR'])

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.0002, random_state=42)

model = Sequential([
    Dense(64, activation='relu', input_shape=(4,)),  # Couche d'entrée avec 3 nœuds
    Dense(64, activation='relu'),  # Couche cachée avec 64 nœuds et fonction d'activation relu
    Dense(3, activation='softmax')  # Couche de sortie avec 3 nœuds et fonction d'activation softmax
])

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

model.compile(
    loss=tf.keras.losses.CategoricalCrossentropy(),
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    metrics=['accuracy']
)

history = model.fit(X_train, Y_train, epochs=50, validation_data=(X_test, Y_test))
predictions = model.predict(X_test)

Y_test_category = Y_test.idxmax(axis=1)
predicted_categories = pd.Series(predictions.argmax(axis=1), index=X_test.index).map({0: 'H', 1: 'D', 2: 'A'})
max_probabilities = pd.Series(np.max(predictions, axis=1), index=X_test.index)

results_df = pd.DataFrame(X_test, columns=['BH', 'BD', 'BA'])
results_df['Div'] = df.loc[X_test.index, 'Div']
results_df['Date'] = df.loc[X_test.index, 'Date']
results_df['HomeTeam'] = df.loc[X_test.index, 'HomeTeam']
results_df['AwayTeam'] = df.loc[X_test.index, 'AwayTeam']
results_df['FTR'] = Y_test_category  # Ajout des étiquettes réelles
results_df['Predictions'] = predicted_categories  # Ajout des prédictions
results_df['MaxProb'] = max_probabilities  # Ajout des probabilités maximales


#put dataframe into excel file
# results_df.to_excel('results.xlsx')
results_df.to_csv('results.csv', sep=';')

total_rows = len(results_df)
num_correct_predictions = len(results_df[(results_df['FTR'] == results_df['Predictions'])])

logging.debug(f'Accuracy: {num_correct_predictions / total_rows * 100}%')

# Affichage de la perte (loss) pendant l'entraînement
plt.plot(history.history['loss'], label='Loss')
plt.title('Training Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.show()

# Affichage de la précision (accuracy) pendant l'entraînement
plt.plot(history.history['accuracy'], label='Accuracy')
plt.title('Training Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()  
plt.show()
