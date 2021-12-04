#%%
import pandas as pd
log = open('log.txt','w')
df = pd.read_csv('BeijingPM20100101_20151231.csv')
df_year_PM = df.groupby('year').agg({'PM_Dongsi':'mean','PM_Dongsihuan':'mean','PM_Nongzhanguan':'mean','PM_US Post':'mean'})
df_year_PM["PM_avg"] = df_year_PM.mean(axis=1)
print(df_year_PM["PM_avg"])
log.write(df_year_PM["PM_avg"].to_string())
df_year_PM[["PM_avg"]].plot()

df_month_PM = df.groupby(['year','month']).agg({'PM_Dongsi':'mean','PM_Dongsihuan':'mean','PM_Nongzhanguan':'mean','PM_US Post':'mean'})
df_month_PM["PM_avg"] = df_month_PM.mean(axis=1)
print(df_month_PM["PM_avg"])
log.write(df_month_PM["PM_avg"].to_string())
df_month_PM[["PM_avg"]].plot()

df_month_TEMP = df.groupby(['year','month']).agg({'TEMP':'mean'})
print(df_month_TEMP)
log.write(df_month_TEMP.to_string())
df_month_TEMP.plot()
# %%
