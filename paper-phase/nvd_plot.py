import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the CVE Details vulnerabilities by type page
url = 'https://www.cvedetails.com/vulnerabilities-by-types.php'

# Send a request to fetch the HTML content of the page
response = requests.get(url)
response.raise_for_status()  # Check that the request was successful

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table containing the vulnerabilities data
table = soup.find('table', {'class': 'stats'})

# Extract the data
data = []
headers = [header.text for header in table.find_all('th')]
for row in table.find_all('tr')[1:]:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append(cols)

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data, columns=headers)

# Clean and process the data
df = df.rename(columns={'Number Of Vulns': 'Count'})
df['Count'] = df['Count'].str.replace(',', '').astype(int)
df['Year'] = pd.to_datetime(df['Year'], format='%Y').dt.year

# Save the data to a CSV file
df.to_csv('vulnerabilities.csv', index=False)

print('Data has been saved to vulnerabilities.csv')

