# import pandas library, "create_engine" function and "types" module from sqlalchemy library
import pandas as pd
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






