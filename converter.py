import pandas as pd

# Load the JSON data into a pandas DataFrame
df = pd.read_json('output.json')

# Define the fields to extract based on your specification
fields_to_extract = [
    "timestamp", "devname", "devid", "date", "time", 
    "type", "subtype", "level", "srcip", "srcport", 
    "srcintf", "srcintfrole", "dstip", "dstport", 
    "dstintf", "dstintfrole", "proto", "policyid", 
    "service", "dstcountry", "srccountry", "trandisp", 
    "duration", "sentbyte", "rcvdbyte", "sentpkt", 
    "appcat", "ip_address", "action"
]

# Extract the relevant columns
extracted_df = df[fields_to_extract]

# Remove extra quotation marks
extracted_df = extracted_df.applymap(lambda x: x.strip('\"') if isinstance(x, str) else x)

# Convert timestamp to a datetime format
extracted_df['timestamp'] = pd.to_datetime(extracted_df['timestamp'], unit='s')

# Ensure that 'date' and 'time' are strings before combining them
extracted_df['date'] = extracted_df['date'].astype(str)
extracted_df['time'] = extracted_df['time'].astype(str)

# Combine 'date' and 'time' into a single datetime column
extracted_df['datetime'] = pd.to_datetime(extracted_df['date'] + ' ' + extracted_df['time'])

# Drop the original 'date' and 'time' columns since they're now combined into 'datetime'
extracted_df.drop(columns=['date', 'time'], inplace=True)

# Convert categorical columns to category dtype
categorical_columns = [
    "devname", "devid", "type", "subtype", "level", 
    "srcintf", "srcintfrole", "dstintf", "dstintfrole", 
    "service", "dstcountry", "srccountry", "trandisp", 
    "appcat", "ip_address"
]
for col in categorical_columns:
    extracted_df[col] = extracted_df[col].astype('category')

# Convert numerical columns to appropriate types
numerical_columns = ["srcport", "dstport", "proto", "policyid", "duration", "sentbyte", "rcvdbyte", "sentpkt"]
for col in numerical_columns:
    extracted_df[col] = pd.to_numeric(extracted_df[col])

# Save the cleaned DataFrame to a CSV file
extracted_df.to_csv('extracted_data_clean.csv', index=False)

# Display the cleaned DataFrame
print(extracted_df.head())



