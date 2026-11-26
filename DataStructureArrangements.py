import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

# Conversion rates to USD (Nov 24, 2026)
rates_to_usd = {
    "EUR": 1.097025,
    "GBP": 1.309820,
    "JPY": 0.006283,
    "HKD": 0.127523,
    "CHF": 1.194934,
}
# Create USD columns for each stock

#CSV 1
asml=pd.read_csv("close_ASML_EUR.csv",skipinitialspace=True,index_col=0)
#sorts dates so that it moves in order 
asml.index = pd.to_datetime(asml.index)
asml = asml.sort_index()

#replace the non numbers with nothing turns it into a float and fil the one before 
asml["ASML (EUR)"]=(asml["ASML (EUR)"].str.replace(",","",regex=False).str.replace("€","",regex=False)).drop_duplicates().astype(float).ffill()

#catches outliners using satrand div points catching extreme spikes
asmlbydcol = asml["ASML (EUR)"]
z_score = (asmlbydcol - asmlbydcol.mean()) / asmlbydcol.std()
# Keep values within 3 standard deviations; replace outliers with previous price
asml["ASML (EUR)"] = asmlbydcol.where(z_score.abs() <= 3).ffill()

#currency conversion 
asml["ASML (USD)"] = asml["ASML (EUR)"] * rates_to_usd["EUR"]

#plotting
plt.figure(figsize=(10,6))
plt.plot(asml.index,asml["ASML (USD)"])
plt.title("Prices Over Time")
plt.xlabel("Date")
plt.ylabel("Price ($)")
plt.grid(True)
plt.show()

#CSV 2
Shell=pd.read_csv("close_Shell_GBP.csv",skipinitialspace=True,index_col=0)
#sorts dates so that it moves in order 
Shell.index = pd.to_datetime(Shell.index)
Shell = Shell.sort_index()

#replace the non numbers with nothing turns it into a float and fil the one before 
Shell["Shell (GBP)"]=(Shell["Shell (GBP)"].str.replace(",","",regex=False).str.replace("£","",regex=False)).drop_duplicates().astype(float).ffill()

Shellbydcol = Shell["Shell (GBP)"]
z_score = (Shellbydcol - Shellbydcol.mean()) / Shellbydcol.std()

# Keep values within 3 standard deviations; replace outliers with previous price
Shell["Shell (GBP)"] = Shellbydcol.where(z_score.abs() <= 3).ffill()

Shell["Shell (USD)"] = Shell["Shell (GBP)"] * rates_to_usd["GBP"]

#plotting
plt.figure(figsize=(10,6))
plt.plot(Shell.index,Shell["Shell (USD)"])
plt.title("Prices Over Time")
plt.xlabel("Date")
plt.ylabel("Price ($)")
plt.grid(True)
plt.show()

#CSV 3
dftx=pd.read_csv("close_DFTX_JPY.csv",skipinitialspace=True,index_col=0)
#sorts dates so that it moves in order 
dftx.index = pd.to_datetime(dftx.index)
dftx = dftx.sort_index()

#replace the non numbers with nothing turns it into a float and fil the one before 
dftx["DFTX (JPY)"]=(dftx["DFTX (JPY)"].astype(float).ffill())

dftxbydcol = dftx["DFTX (JPY)"]
z_score = (dftxbydcol - dftxbydcol.mean()) / dftxbydcol.std()

# Keep values within 3 standard deviations; replace outliers with previous price
dftx["DTFX (JPY)"] = dftxbydcol.where(z_score.abs() <= 3).ffill()

dftx["DFTX (USD)"] = dftx["DFTX (JPY)"] * rates_to_usd["JPY"]

#plotting
plt.figure(figsize=(10,6))
plt.plot(dftx.index,dftx["DFTX (USD)"])
plt.title("Prices Over Time")
plt.xlabel("Date")
plt.ylabel("Price ($)")
plt.grid(True)
plt.show()

#CSV 4
byd=pd.read_csv("close_BYD_HKD.csv",skipinitialspace=True,index_col=0)
#sorts dates so that it moves in order 
byd.index = pd.to_datetime(byd.index)
byd = byd.sort_index()

#replace the non numbers with nothing turns it into a float and fil the one before 
byd["BYD (HKD)"]=(byd["BYD (HKD)"].astype(float).ffill())

bydcol = byd["BYD (HKD)"]
z_score = (bydcol - bydcol.mean()) / bydcol.std()
# Keep values within 3 standard deviations; replace outliers with previous price
byd["BYD (HKD)"] = bydcol.where(z_score.abs() <= 3).ffill()

byd["BYD (USD)"] = byd["BYD (HKD)"] * rates_to_usd["HKD"]

#plotting
plt.figure(figsize=(10,6))
plt.plot(byd.index,byd["BYD (USD)"])
plt.title("Prices Over Time")
plt.xlabel("Date")
plt.ylabel("Price ($)")
plt.grid(True)
plt.show()

#CSV 5
bac=pd.read_csv("close_BAC_CHF.csv",skipinitialspace=True,index_col=0)
#sorts dates so that it moves in order 
bac.index = pd.to_datetime(bac.index)
bac = bac.sort_index()

#replace the non numbers with nothing turns it into a float and fil the one before 
bac["BAC (CHF)"]=(bac["BAC (CHF)"].astype(float).ffill())

baccaol = bac["BAC (CHF)"]
z_score = (baccaol - baccaol.mean()) / baccaol.std()

# Keep values within 3 standard deviations; replace outliers with previous price
bac["BAC (CHF)"] = baccaol.where(z_score.abs() <= 3).ffill()

bac["BAC (USD)"] = bac["BAC (CHF)"] * rates_to_usd["CHF"]

#plotting
plt.figure(figsize=(10,6))
plt.plot(bac.index,bac["BAC (USD)"])
plt.title("Prices Over Time")
plt.xlabel("Date")
plt.ylabel("Price ($)")
plt.grid(True)
plt.show()
