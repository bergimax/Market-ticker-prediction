#!/usr/bin/env python
# coding: utf-8

import requests

url = 'http://localhost:9696/predict'
#from GC[5000]
day= '2020-08-10'
open = 2026.400024
high = 2043.800049
low = 2017.5
close = 2024.400024
volume = 233

diff_oc = abs(open - close)  
diff_hl = abs(high - low) 
diff_ol = abs(open - low) 
diff_oh = abs(open - high)
diff_cl = abs(close - low) 
diff_ch = abs(close - high)

market = {
  'data': day, 
  'close': close, 
  'volume': volume, 
  'diff_oc': diff_oc, 
  'diff_hl': diff_hl, 
  'diff_ol': diff_ol, 
  'diff_oh': diff_oh, 
  'diff_cl': diff_cl, 
  'diff_ch': diff_ch
}


requests.post(url, json=market)

requests.post(url, json=market).json()

response = requests.post(url, json=market).json()

if(response['commodity'] == 0):
    com = 'Gold'
elif(response['commodity'] == 1):
    com = 'Silver'    
elif(response['commodity'] == 2):
    com = 'Platinum'
elif(response['commodity'] == 3):
    com = 'copper' 
elif(response['commodity'] == 4):
    com = 'Palladium'
else:
    com = 'no commodity found'
print('The data are of the commodity ', com )
