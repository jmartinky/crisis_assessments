import pandas as pd
import numpy as np
import seaborn as sns
from datetime import datetime, timedelta, date
import datetime as dt
import matplotlib.pyplot as plt
from dateutil.relativedelta import relativedelta


## read data into object
data = pd.read_excel("D:/PY_tests/##_sandbox/2020_03_THRU_05_cleaned.xlsx")

## date formatting
bd = data['Date of Birth']
data['ass_date'] = data['ass_date'].astype('string')
data['ass_date'] = data['ass_date'].str.slice(0, 10)
assessment = data['ass_date'].astype('datetime64[ns]')

## calc age at encounter from (ass_date - Date of Birth)/365.2425
age_at_encounter = ((assessment - bd).dt.days // 365.2425).astype('int')

## primary problem count
prob_count = pd.Series(data['prime_prob']).value_counts().nlargest(5)
#print(prob_count)

## alt to hospital count
alt_hosp_count = pd.Series(data['alt_to_hosp']).value_counts().nlargest(5)
#print(alt_hosp_count)

## referral count
referral_count = pd.Series(data['referral']).value_counts().nlargest(5)
#print(referral_count)

## count top fix DX from DX_1_1 thru DX_1_10
DX_list = []
DX_list.append(data['DX_1_1'])
DX_list.append(data['DX_1_2'])
DX_list.append(data['DX_1_3'])
DX_list.append(data['DX_1_4'])
DX_list.append(data['DX_1_5'])
DX_list.append(data['DX_1_6'])
DX_list.append(data['DX_1_7'])
DX_list.append(data['DX_1_8'])
DX_list.append(data['DX_1_9'])
DX_list.append(data['DX_1_10'])
DX_codes = pd.concat(DX_list)
DX_codes = pd.Series(DX_codes).value_counts().nlargest(5)
print(DX_codes)

#print('Unique SSN:', data.SSN.nunique())
#print('Desc age_at_encounter:', age_at_encounter.describe().T)
#print(data['Gender'].value_counts(normalize=True))
#print(data['Race'].value_counts(normalize=True))
