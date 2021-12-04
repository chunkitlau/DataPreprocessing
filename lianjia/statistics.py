import pandas as pd
df = pd.read_csv('MyData.csv')

maxTotalPriceId = df["totalPrice"].idxmax()
maxTotalPriceRow = df.iloc[maxTotalPriceId,:]

minTotalPriceId = df["totalPrice"].idxmin()
minTotalPriceRow = df.iloc[minTotalPriceId,:]

medianTotalPrice = df["totalPrice"].median()

maxAvgPriceId = df["avgPrice"].idxmax()
maxAvgPriceRow = df.iloc[maxAvgPriceId,:]

minAvgPriceId = df["avgPrice"].idxmin()
minAvgPriceRow = df.iloc[minAvgPriceId,:]

medianAvgPrice = df["avgPrice"].median()

print("Max Total Price: ")
print(maxTotalPriceRow)
print("Min Total Price: ")
print(minTotalPriceRow)
print("Median Total Price: ")
print(medianTotalPrice)
print("Max Avg Price: ")
print(maxAvgPriceRow)
print("Min Avg Price: ")
print(minAvgPriceRow)
print("Median Avg Price: ")
print(medianAvgPrice)