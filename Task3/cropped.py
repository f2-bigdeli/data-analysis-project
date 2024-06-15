# .................. Cropping Data ..............................

# Import pandas library 
import pandas as pd

# Read data from the CSV files and store them in DataFrames
dataframe1 = pd.read_csv("airquality1.csv")
dataframe2 = pd.read_csv("airquality2.csv")
dataframe3 = pd.read_csv("airquality3.csv")

# Convert the "Date_Time" column in each DataFrame to datetime format
# Use errors='coerce' to handle out-of-bounds values
dataframe1["Date_Time"] = pd.to_datetime(dataframe1["Date_Time"], errors='coerce')
dataframe2["Date_Time"] = pd.to_datetime(dataframe2["Date_Time"], errors='coerce')
dataframe3["Date_Time"] = pd.to_datetime(dataframe3["Date_Time"], errors='coerce')

# Filter rows in each DataFrame based on the specified date range
df1 = dataframe1[(dataframe1["Date_Time"] >= "2015-01-01") & (dataframe1["Date_Time"] < "2023-10-23")]
df2 = dataframe2[(dataframe2["Date_Time"] >= "2015-01-01") & (dataframe2["Date_Time"] < "2023-10-23")]
df3 = dataframe3[(dataframe3["Date_Time"] >= "2015-01-01") & (dataframe3["Date_Time"] < "2023-10-23")]

# Save the new DataFrames as CSV files without including row indexes
df1.to_csv("pollution1.csv", index=False)
print(f"new file saved as {'pollution1.csv'}")

df2.to_csv("pollution2.csv", index=False)
print(f"new file saved as {'pollution2.csv'}")

df3.to_csv("pollution3.csv", index=False)
print(f"new file saved as {'pollution3.csv'}")


# ...................... Merging Data....................

# Read data from the CSV files and store them in a DataFrames
df1 = pd.read_csv("pollution1.csv")
df2 = pd.read_csv("pollution2.csv")
df3 = pd.read_csv("pollution3.csv")

# Combine the three DataFrames into a single DataFrame
merged = pd.concat([df1, df2, df3])

# Save the new DataFrame as a CSV file without including row indexes.
merged.to_csv("pollution4.csv", index=False)

# Print a message indicating that a new CSV file has been saved
print(f"Merged file saved as {'pollution4.csv'}")

# .................. Remove Rows With Empty Site_ID ..................

# Read the CSV file into a pandas DataFrame
df = pd.read_csv("pollution4.csv")

# Count the number of rows with null Site_ID before removal
count_before = df["Site_ID"].isna().sum()

# Check for empty Site_ID and remove corresponding rows
df = df.dropna(subset=["Site_ID"])

# Count the number of rows with null Site_ID after removal
count_after = df["Site_ID"].isna().sum()

# Save the modified DataFrame back to a new CSV file
df.to_csv("clean.csv", index=False)

# Calculating the number of removed rows
removed_rows_count = count_before - count_after

# Print the number of rows removed due to null Site_ID
print(f"Removed {removed_rows_count} rows due to null Site_ID.")

# .....................remove duplicates................ 

# Read the CSV file into a DataFrame
df = pd.read_csv("clean.csv")

# calculate the number of duplicate rows based on the first two columns
duplicate_count = df.duplicated(subset = df.columns[:2]).sum()

# Print the number of duplicate rows based on the first two columns
print(f"Number of duplicate rows: {duplicate_count}")

# Remove duplicates based on the first two columns, keeping the last occurrence
df_no_duplicates = df.drop_duplicates(subset = df.columns[:2], keep="last")

# Save the DataFrame without duplicates to a new CSV file
df_no_duplicates.to_csv("no_duplicates.csv", index=False)

# Print a message indicating that the new CSV file without duplicates has been saved
print(f"DataFrame without duplicates saved as {'no_duplicates.csv'}")

# ................... Remove Negative Values......................

# Read the CSV file into a DataFrame
df = pd.read_csv("no_duplicates.csv")

# Define a list of columns to check for negative values
columns_to_check = ['NOx', 'NO2', 'NO', 'PM10', 'O3', 'NVPM10', 'VPM10', 'NVPM2_5', 'PM2_5', 'VPM2_5', 'CO', 'RH', 'SO2']  

# Create a boolean mask to identify rows with negative values in any of the specified columns
negative_mask = (df[columns_to_check] < 0).any(axis=1)

# Create a new DataFrame by excluding rows with negative values
df_no_negative = df[~negative_mask]

# Save the DataFrame without rows containing negative values to a new CSV file
df_no_negative.to_csv("no_negative.csv", index=False)

# Print a message indicating that the new CSV file without negative values has been saved
print(f"DataFrame without rows containing negative values saved as {'no_negative.csv'}")

#...................... Replace Empty Cells With Null ...........

# Read the CSV file into a DataFrame
df = pd.read_csv("no_negative.csv")

# Use the fillna() method to replace empty cells with NULL.
df.fillna("NULL", inplace=True)

# Save the DataFrame to a new CSV file
df.to_csv("cropped and cleansed.csv", index=False)

 # Print a message indicating that the new CSV file without empty cells has been saved
print(f"DataFrame without empty cells saved as {'cropped and cleansed.csv'}")

# ........................ Import CSV File into Table .......................

# import "create_engine" function and "types" module from sqlalchemy library
from sqlalchemy import create_engine, types

# Database connection details
db_username = "root"
db_password = None  
db_host = "localhost"
db_name = "air_quality"
table_name = "measurement"

# Read CSV into a pandas DataFrame
df = pd.read_csv("cropped and cleansed.csv", parse_dates=["Date_Time"])

# Define SQLAlchemy types for each column
sql_types = {
    'Date_Time': types.DateTime(),
    'SiteID': types.Integer(),
    'ObjectId': types.Integer(),
    'ObjectId2': types.Integer(),
    'NOx': types.Float(precision=12),
    'NO2': types.Float(precision=12),
    'NO': types.Float(precision=12),
    'PM10': types.Float(precision=12),
    'O3': types.Float(precision=12),
    'Temperature': types.Float(precision=12),
    'NVPM10': types.Float(precision=12),
    'VPM10': types.Float(precision=12),
    'NVPM2_5': types.Float(precision=12),
    'PM2_5': types.Float(precision=12),
    'VPM2_5': types.Float(precision=12),
    'CO': types.Float(precision=12),
    'RH': types.Float(precision=12),
    'Pressure': types.Float(precision=12),
    'SO2': types.Float(precision=12)
}

# Create a connection to MySQL
engine = create_engine(f'mysql+pymysql://{db_username}:@{db_host}/{db_name}')

# Insert data into MySQL table
df.to_sql(name=table_name, con=engine, if_exists="replace", index=False, dtype=sql_types)

# Print a message indicating that data imported to the table
print(f"Data imported into the {table_name} table successfully.")






