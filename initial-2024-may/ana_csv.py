import csv
import re
import time

start_time = time.time()

input_file = "/mnt/suraj/KSS/Studies/RVCE/CVE/csv_data.csv"

cve_counts = {
    "Offline Interference": 0,
    "Password Access": 0, 
    "Running Distributions/Products": 0,
    "Large Scale Business": 0
}

cve_severities = {
    ("Offline Interference", "Low"): 0,
    ("Offline Interference", "Medium"): 0,
    ("Offline Interference", "High"): 0,
    ("Offline Interference", "Critical"): 0,
    ("Password Access", "Low"): 0,
    ("Password Access", "Medium"): 0,
    ("Password Access", "High"): 0,
    ("Password Access", "Critical"): 0,
    ("Running Distributions/Products", "Low"): 0,
    ("Running Distributions/Products", "Medium"): 0,
    ("Running Distributions/Products", "High"): 0,
    ("Running Distributions/Products", "Critical"): 0,
    ("Large Scale Business", "Low"): 0,
    ("Large Scale Business", "Medium"): 0,
    ("Large Scale Business", "High"): 0,
    ("Large Scale Business", "Critical"): 0,
}

# categories and their associated keywords
keywords = {
    "Offline Interference": ["offline interference"],
    "Password Access": ["password", "authentication"],
    "Running Distributions/Products": ["running distribution", "affected product"],
    "Large Scale Business": ["large scale business", "enterprise"]
}

with open(input_file, newline='', encoding=utf-8) as csvfile:  # Specify 'latin-1' encoding
    reader = csv.reader(csvfile)
    for _ in range(8):
        next(reader)
    
    for row in reader:
        cve_id, status, description, references, phase, votes, comments = row
        
        # severity based on "Status" field
        if status == "Entry":
            severity = "High"
        elif status == "Candidate":
            severity = "Medium"
        else:
            severity = "Low"

        # description for keywords
        for category, category_keywords in keywords.items():
            for keyword in category_keywords:
                if re.search(r'\b' + re.escape(keyword) + r'\b', description, re.IGNORECASE):
                    cve_counts[category] += 1
                    cve_severities[(category, severity)] += 1
                    break

print("-----------------------------------------------------------------")
print("CVE Frequency and Severity by Category:")
print("-----------------------------------------------------------------")

for category in keywords.keys():
    print(f"Category: {category}")
    print("----------------------")
    print(f"Frequency: {cve_counts[category]}")

    for severity in ["Low", "Medium", "High", "Critical"]:
        print(f"  {severity}: {cve_severities[(category, severity)]}")
    print("")

execution_time = time.time() - start_time
print(f"Script execution time: {execution_time:.2f} seconds")
