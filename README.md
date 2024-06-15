# Air Quality Data Analysis

## Overview
This repository contains a comprehensive project for analyzing air quality data from Bristol, spanning from 1993 to October 2023. The project involves six tasks that demonstrate practical applications of relational and non-relational database management systems, data preprocessing, and query writing. Each task is documented and includes corresponding output files and scripts.

## Files and Folders

### Data Files
- **airquality1.csv, airquality2.csv , airquality3.csv**: The main dataset containing air quality measurements from 19 monitoring stations in Bristol.

### Documentation
- **Air_Quality_Project.docx**: A detailed document explaining the tasks and outputs.

### Tasks

#### Task 1: Organize and Model the Data
- **Description**: Group the detectors by constituency and design a normalized Entity Relationship (ER) model that includes all data items.
- **Output**:
  - `pollution-er.png`: ER diagram.
  - `entity.png`: Schematic image of entities and relationships.

#### Task 2: Forward Engineer the ER Model to a MySQL Database
- **Description**: Create tables and fields in MySQL to hold the data, with appropriate primary and foreign keys.
- **Output**:
  - `pollution.sql`: SQL file with table and attribute definitions.

#### Task 3: Crop and Cleanse the Data
- **Description**: Cleanse the dataset to ensure dates fall between 1st January 2015 and 22nd October 2023.
- **Output**:
  - `cropped.zip`: ZIP file containing the cleansed data in CSV format.
  - `cropped.py`: Python script for cleaning and cropping tasks.
  - `python_Output.png`: Screenshot of Python script output.
  - `cleaning.png`: Image showing cleaning and cropping steps.

#### Task 4: Populate the MySQL Database Tables
- **Description**: Import the cleansed datasets into MySQL tables.
- **Output**:
  - `import.py`: Python script for importing data into MySQL.
  - `constituency.png`, `measurement.png`, `schema.png`, `site.png`: Screenshots of populated tables.

#### Task 5: Design, Write, and Run SQL Queries
- **Description**: Write and execute SQL queries to extract specific information from the dataset.
- **Queries**:
  1. Highest recorded value of nitrogen oxide (NOx) for 2022.
  2. Mean values of PM2.5 and VPM2.5 by station for 2022 at 08:00 AM.
  3. Mean values of PM2.5 and VPM2.5 by station for all data.
- **Output**:
  - `query-a.sql`, `query-b.sql`, `query-c.sql`: SQL query files.
  - `query_output_a.png`, `query_output_b.png`, `query_output_c.png`: Screenshots of query outputs.

#### Task 6: Model, Implement, and Query a NoSQL Database
- **Description**: Model part of the data for a NoSQL database using MongoDB and implement three example queries.
- **Output**:
  - `nosql.md`: Report with NoSQL queries and their purposes.
  - `mongo-query1.png`, `mongo-query2.png`, `mongo-query3.png`: Screenshots of NoSQL query outputs.

## Prerequisites

### Software
- **MySQL**: For relational database tasks.
- **MongoDB**: For NoSQL database tasks.
- **Python**: For data preprocessing scripts.
- **MySQL Workbench/PhpMyAdmin**: For managing MySQL database.

## How to Use

1. **Clone the repository**:
   ```bash
   git clone https://github.com/f2-bigdeli/data-analysis-project.git
