-- Select the name column in site table (as StationName)
SELECT Name AS StationName,

-- calculate the average of PM2.5 and VPM2.5 values
AVG(`PM2_5`) AS Mean_PM2_5, AVG(`VPM2_5`) AS Mean_VPM2_5 

-- Specify the source table for the query
FROM Measurement 

-- Join the Measurement table with the Site table using the Site_ID and SiteID columns respectively
JOIN Site ON measurement.Site_ID = site.SiteID 

-- Filter the results to include only records from the year 2022 and time '08:00:00'
WHERE YEAR(`Date_Time`) = 2022 
AND TIME(`Date_Time`) = '08:00:00' 

-- Group the results by station name to calculate averages for each station
GROUP BY StationName;