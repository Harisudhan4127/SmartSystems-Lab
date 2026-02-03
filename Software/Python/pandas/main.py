import pandas as pd
import os

# Function to check the ISBN and related details
def to_check(file_path, isbn):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Print the DataFrame's columns to debug
    print(df.columns)
    
    # Check if required columns are present
    required_columns = ['print', 'electronic', 'doi']
    for col in required_columns:
        if col not in df.columns:
            print(f"Missing column: {col}")
            return
    
    # Retrieve the values from the first row
    print_no = df.loc[0, 'print']
    electronic = df.loc[0, 'electronic']
    doi = df.loc[0, 'doi']
    
    print(print_no, '\t', electronic, '\t', doi, 'testing')
    
    # Perform the checks
    if print_no == isbn:
        print('print version are matching ISBN')
    elif electronic == isbn:
        print('Electronic version is matching ISBN')
    elif print_no == electronic:
        print('Both print and electronic versions are matching ISBN')
    elif doi == f"10.1009_oso_{isbn}_001_0001":
        print('DOI is not compatible')
    else:
        print('All checks passed')

# Directory containing the CSV files
file_dir = r"D:\VS_Code\python\pandas\willam"
items = os.listdir(file_dir)
# print(items)

# Process each CSV file in the directory
for item in items:
    if item.endswith('.csv'):
        isbn = item.split('.')[0]
        print(isbn)
        file_path = os.path.join(file_dir, item)
        print(file_path)
        
        # Call the check function for the current file
        to_check(file_path, isbn)
