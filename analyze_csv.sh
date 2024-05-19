#!/bin/bash

# Input CSV file
input_file="/run/media/suraj/KSS/Studies/RVCE/CVE/csv_data.csv"

# Initialize data structures
declare -A cve_counts
declare -A cve_severities

# Define categories and their associated keywords
declare -A keywords=(
  ["Offline Interference"]="offline interference"
  ["Password Access"]="password authentication"
  ["Running Distributions/Products"]="running distribution affected product"
  ["Large Scale Business"]="large scale business enterprise"
)

# Initialize dictionaries
for category in "${!keywords[@]}"; do
  cve_counts["$category"]=0
  for severity in "Low" "Medium" "High" "Critical"; do
    cve_severities["$category,$severity"]=0
  done
done

# Skip header lines
tail -n +9 "$input_file" | while IFS=, read -r cve_id status description references phase votes comments; do
  
  # Determine severity based on "Status" field
  case "$status" in
    "Entry") 
      severity="High" 
      ;;
    "Candidate")
      severity="Medium" 
      ;;
    *) 
      severity="Low"
      ;;
  esac

  # Analyze description for keywords
  for category in "${!keywords[@]}"; do
    for keyword in ${keywords["$category"]}; do
      if [[ "$description" =~ $keyword ]]; then
        cve_counts["$category"]=$((cve_counts["$category"] + 1)) 
        cve_severities["$category,$severity"]=$((cve_severities["$category,$severity"] + 1))
        break 2 # Move to next CVE if a category is found
      fi
    done
  done

done

# Print results
echo "-----------------------------------------------------------------"
echo "CVE Frequency and Severity by Category:"
echo "-----------------------------------------------------------------"

for category in "${!keywords[@]}"; do
  echo "Category: $category"
  echo "----------------------"
  echo "Frequency: ${cve_counts[$category]}"

  # Print severity breakdown
  for severity in "Low" "Medium" "High" "Critical"; do
    echo "  $severity: ${cve_severities["$category,$severity"]}"
  done
  echo ""
done
