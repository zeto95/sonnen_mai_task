import pandas as pd
from pandasql import sqldf

csv_file_path = 'app/measurements.csv'

# 1. Load CSV
# Read CSV to a pandas datafram
df = pd.read_csv(csv_file_path, sep =';')
print(df.head(10))


# 2. Datatypes
# Convert columns to their appropriate data types
print (df.dtypes)
df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
df['grid_purchase'] = pd.to_numeric(df['grid_purchase'], errors='coerce')
df['grid_feedin'] = pd.to_numeric(df['grid_feedin'], errors='coerce')
df['direct_consumption'] = pd.to_numeric(df['direct_consumption'], errors='coerce')
df['date'] = pd.to_datetime(df['date'], errors='coerce')
print (df.dtypes)


# 3. Fillna 
# Get columns with null values
print(df.columns[df.isnull().any()])

df['grid_purchase'].fillna(df['grid_purchase'].median(), inplace=True)
df['grid_feedin'].fillna(df['grid_purchase'].median(), inplace=True)
df = df.drop('direct_consumption', axis=1)

print(df.columns[df.isnull().any()])


# 4. Duplicates 
# Remove duplicates
print (df.duplicated().sum())
df.drop_duplicates(inplace=True)
print (df.duplicated().sum())

# 5. Calculate the total grid_purchase and grid_feedin over all batteries for each hour of the day
df['hour'] = df['timestamp'].dt.hour
query = '''
SELECT hour, SUM(grid_purchase) AS total_grid_purchase, SUM(grid_feedin) AS total_grid_feedin
FROM df
GROUP BY hour
'''
result = sqldf(query, locals())
print(result)

# 6. Add a boolean column to indicate the hour with the highest total_grid_feedin
max_hour = result['total_grid_feedin'].idxmax()
df['is_highest_grid_feed'] = df['hour'] == max_hour

print(df.head(40))

# 7. Write the transformed data to an output file in CSV format
df.to_csv('app/output.csv', index=False)




'''
# To fill na with mean or median 
# Calculate the percentage of outliers
#threshold = 3  # Adjust the threshold as needed
#outliers_percentage = (df[column_name].abs() > threshold).mean() * 100

# Print the percentage of outliers
#print(f"The percentage of outliers in {column_name} is: {outliers_percentage:.2f}%")
# percentage of outliers is 62%

'''