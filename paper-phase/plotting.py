import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the CSV data into a Pandas DataFrame
df = pd.read_csv('cve_data_2013_23.csv')

# 2. Convert 'datePublished' to datetime objects, making all UTC
df['datePublished'] = pd.to_datetime(df['datePublished'], format='ISO8601', utc=True)

# 3. Group by 'cwe_description' and count occurrences per month (using 'ME' for month end)
grouped = df.groupby([pd.Grouper(key='datePublished', freq='ME'), 'cwe_description'])['cwe_description'].count().unstack()

# 4. Plot the data
plt.figure(figsize=(12, 6)) 
grouped.plot(kind='line', xlabel='Date', ylabel='CVE Count', title='CVE Count Over Time by CWE Description')
plt.legend(title='CWE Description')
plt.xticks(rotation=45) 
plt.tight_layout() 
plt.show()
