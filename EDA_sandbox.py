import pandas as pd
import numpy as np
import seaborn as sns
from datetime import datetime, timedelta, date
import datetime as dt
import matplotlib.pyplot as plt
from dateutil.relativedelta import relativedelta

## read data into object
data = pd.read_excel("D:/PY_tests/carey_sandbox/2020_03_THRU_05_cleaned.xlsx")

## date formatting
bd = data['Date of Birth']
data['ass_date'] = data['ass_date'].astype('string')
data['ass_date'] = data['ass_date'].str.slice(0, 10)
assessment = data['ass_date'].astype('datetime64[ns]')
## calc age at encounter from (ass_date - Date of Birth)/365.2425
age_at_encounter = ((assessment - bd).dt.days // 365.2425).astype('int')


print(data.head())
print(data.info())
print(bd)
print(assessment)
print(age_at_encounter)
