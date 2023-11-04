#!/usr/bin/env python
# coding: utf-8

#import

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestRegressor

import pickle

#parameters

output_file = 'mid_term_model.bin'

max_depth = 20
min_samp_leaf = 5
n_estim = 60

#Data preparation

df = pd.read_csv("all_commodities_data.csv")

del df['ticker']

ticker_com = {
    'Gold': 0, 
    'Silver': 1,
    'Platinum': 2,
    'Copper': 3,
    'Palladium': 4
}
df.commodity = df.commodity.map(ticker_com) #mappa la modifica

df['diff_oc'] = abs(df['open'] - df['close'])  
df['diff_hl'] = abs(df['high'] - df['low']) 
df['diff_ol'] = abs(df['open'] - df['low']) 
df['diff_oh'] = abs(df['open'] - df['high'])
df['diff_cl'] = abs(df['close'] - df['low']) 
df['diff_ch'] = abs(df['close'] - df['high'])

del df['open']
del df['high']
del df['low']

#split in train - val - test
 
df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=11)
df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=11)

#reset the index of the new datasets
df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)
df_full_train = df_full_train.reset_index(drop=True)

#create the target of each DS
y_train = df_train.commodity
y_val = df_val.commodity
y_test = df_test.commodity
y_full_train = df_full_train.commodity

del df_train['commodity']
del df_val['commodity']
del df_test['commodity']
del df_full_train['commodity']

def rmse(y, y_pred):
    error = y - y_pred #calcolo errore tra i 2 array
    se = error **2 #quadrato della differenza
    mse = se.mean() #media della differenza
    return np.sqrt(mse) #radice del valore medio

#RANDOM FOREST

train_dicts = df_train.to_dict(orient='records')
dv = DictVectorizer(sparse=False)
X_train = dv.fit_transform(train_dicts)
rf = RandomForestRegressor(n_estimators = n_estim, max_depth = max_depth, min_samples_leaf = min_samp_leaf, random_state=1) 
rf.fit(X_train, y_train)

val_dicts = df_val.to_dict(orient='records')
X_val = dv.transform(val_dicts)
y_pred = rf.predict(X_val)
_rmse = rmse(y_val, y_pred)
print((_rmse))
        
#train
dicts_ft = df_full_train.to_dict(orient='records')
dv = DictVectorizer(sparse = False)
X_full_train = dv.fit_transform(dicts_ft)
    
rf = RandomForestRegressor(n_estimators = n_estim, max_depth = max_depth, min_samples_leaf = min_samp_leaf, random_state=1)
rf.fit(X_full_train, y_full_train)
#predict
dicts_test = df_test.to_dict(orient='records')
   
X_test = dv.transform(dicts_test)
y_pred = rf.predict(X_test)

_rmse = rmse(y_test, y_pred)
print((_rmse))

#SAVING THE MODEL

output_file = 'mid_term_model.bin'

with open(output_file, 'wb') as f_out: 
    pickle.dump((dv, rf), f_out)

print(f'the model is saved to {output_file}')