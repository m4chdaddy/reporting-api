import pandas as pd

# Load the CSV file
file_path = 'veracode_data_dump.csv'  # Replace with your CSV file path
df = pd.read_csv(file_path)

# Filter the DataFrame for rows where the app_name NEEDS TO BE ENTERED
filtered_df = df[df['app_name'] == ['<INSERT_APPLICATION PROFILE NAME>']

# Save the filtered data to a new CSV file
output_file_path = 'application.csv'  # Replace with your desired output file path
filtered_df.to_csv(output_file_path, index=False)

