import pandas as pd

# Load the 'Open' status CSV file
open_file_path = 'Open-Flaws.csv'  # Replace with the path to your 'Open' status CSV file
open_df = pd.read_csv(open_file_path)

# Count the number of occurrences of each severity level (3, 4, 5)
severity_counts = open_df['severity'].value_counts().reindex([3, 4, 5], fill_value=0)

# Extract counts for 3's, 4's, and 5's
medium_count = severity_counts.get(3, 0)
high_count = severity_counts.get(4, 0)
very_high_count = severity_counts.get(5, 0)

# Output the counts
print(f"Medium: {medium_count}")
print(f"High: {high_count}")
print(f"Very High: {very_high_count}")

