import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn import metrics

# Load the data
input_file = "/mnt/KSS/Studies/RVCE/CVE/initial-2024-may/filetered cve.csv"
df = pd.read_csv(input_file)

# Check for necessary columns
assert 'attack_description' in df.columns, "CSV must contain 'attack_description' column."
assert 'cwe_code' in df.columns, "CSV must contain 'cwe_code' column."
assert 'cwe_name' in df.columns, "CSV must contain 'cwe_name' column."

# Preprocess the data
X = df['attack_description']
y = df[['cwe_code', 'cwe_name']]  # Target variables

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build the pipeline with TF-IDF Vectorizer and Naive Bayes Classifier
model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', MultinomialNB())
])

# Train the model
model.fit(X_train, y_train['cwe_code'])

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
print("Classification Report:")
print(metrics.classification_report(y_test['cwe_code'], y_pred))

# Function to predict CWE code and name for new attack description
def predict_cwe(attack_description):
    cwe_code = model.predict([attack_description])[0]
    cwe_name = df[df['cwe_code'] == cwe_code]['cwe_name'].values[0]
    return cwe_code, cwe_name

# Example usage
attack_description = "Example attack description"
cwe_code, cwe_name = predict_cwe(attack_description)
print(f"CWE Code: {cwe_code}, CWE Name: {cwe_name}")

