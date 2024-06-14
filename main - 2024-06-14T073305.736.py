import pandas as pd
from datetime import datetime

# Load the dataset (assumed to be in CSV format)
# Example CSV columns: ['TransactionID', 'Date', 'PropertyType', 'Address', 'City', 'State', 'ZipCode', 'Price']

data = pd.read_csv('west_virginia_real_estate_transactions.csv')

# Filter for single-family houses bought in the past year
one_year_ago = datetime.now().replace(year=datetime.now().year - 1)

filtered_data = data[(data['PropertyType'] == 'Single Family') & 
                     (pd.to_datetime(data['Date']) > one_year_ago) & 
                     (data['State'] == 'WV')]

# Group by city or county to find the area with the most transactions
transactions_by_city = filtered_data.groupby('City').size().reset_index(name='TransactionCount')

# Sort the results by the number of transactions
sorted_transactions = transactions_by_city.sort_values(by='TransactionCount', ascending=False)

# Print the top 10 cities with the most single-family house transactions
print(sorted_transactions.head(10))

# Save the results to a CSV file
sorted_transactions.to_csv('most_single_family_houses_bought_in_wv.csv', index=False)
