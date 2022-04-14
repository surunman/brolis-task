## inefficient code, which calculates max value of z1_32 every 5 seconds

import numpy as np
import pandas as pd
import datetime


window_size = 5 #in seconds

## import data
dff = pd.read_csv(("data_for_code_efficiency.csv"))
dff['datetime'] = pd.to_datetime(dff['datetime'])


time1 = datetime.datetime.now()

#split the time into periods

t1 = dff['datetime'].min()  
t2 = t1 + np.timedelta64(window_size, 's')
period = 0

while t1 <= dff['datetime'].max():
    dff.loc[(dff['datetime'] >= t1) & (dff['datetime'] < t2), 'Period'] = period
    period = period + 1
    t1 = t2
    t2 = t2 + np.timedelta64(window_size, 's')

# for every period, calculate maximum value of z1_32 
# and middle value of time
dff_max = pd.DataFrame()
for period in dff['Period'].unique():
    max_value = dff[dff['Period'] == period]['z1_32'].max()
    times = dff[dff['Period'] == period]['datetime']
    middle_time = times.iloc[len(times) // 2]
    dff_max_period = pd.DataFrame({'datetime': middle_time,
                                  'z1_32': max_value}, index = [0])
    dff_max = dff_max.append(dff_max_period)
dff_max = dff_max.reset_index(drop = True)   

time2 = datetime.datetime.now()
print(dff_max['z1_32'].mean())

print(time2 - time1)
