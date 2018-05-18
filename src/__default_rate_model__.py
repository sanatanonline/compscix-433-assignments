import pandas as pd
import matplotlib.pyplot as plt

from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# Load the data from the excel sheet
df = pd.read_excel(open('../data/peps3xx.xls', 'rb'), sheet_name='Sheet1')
print(df)
print(type(df))

# Plot the relationship graphs
# plt.scatter(df.Num, df.Drate)
# plt.show()

# plt.scatter(df.Denom, df.Drate)
# plt.show()

# plt.bar(df.ProgLength, df.Drate)
# plt.show()

# plt.bar(df.EthnicCode, df.Drate)
# plt.show()

# Create a linear model
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(df.Drate, df.EthnicCode)

# predictions = regr.predict(df)

# print("Mean squared error: %.2f" % mean_squared_error(df.Drate, predictions))




