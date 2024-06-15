-- Specify the columns to be included in the result set
SELECT Date_Time, Name AS StationName, NOx

-- Specify the source table for the query
FROM Measurement 

-- Join the Measurement table with the Site table using the Site_ID and SiteID columns respectively
JOIN Site ON measurement.Site_ID = site.SiteID 

-- Filter the results to only include records from the year 2022
WHERE YEAR(Date_Time) = 2022 

-- Order the results in descending order based on the NOx column
ORDER BY NOx DESC 

-- Limit the result set to only the top 1 record with the highest NOx value
LIMIT 1;