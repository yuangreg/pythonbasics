import pandas as pd
import numpy as np

data = np.linspace(0, 10, 24).reshape(6, 4)
columns = ['A', 'B', 'C', 'D']

# Create pandas data frame
data = pd.DataFrame(data, columns=columns)
data_copy = data.copy()

# Add a new entry
last_row = data.index.size
data.loc[last_row] = [10, 10, np.nan, 10]
# Combining panda data frames
df_merge = pd.concat([data, data_copy], ignore_index=True)

# Handling missing data
df_drop = data.dropna(how='any')
df_fill = data.fillna(value=5.0)

# Get numpy data from panda data frame
data_new = df_merge.to_numpy()

# Save and Load data frames
data.to_csv('./data.csv')
data_csv = pd.read_csv('./data.csv', index_col=0, header=0)


data.to_excel('./data.xlsx', sheet_name='Sheet1')
data_excel = pd.read_excel('./data.xlsx', 'Sheet1', index_col=0, header=0)


data.to_json('./data.json')
data_json = pd.read_json('./data.json')


data.to_html('./data.html')
data_html = pd.read_html('./data.html', index_col=0, header=0)[0]


data.to_pickle('./data.pickle')
data_pickle = pd.read_pickle('./data.pickle')
print(data_pickle)




