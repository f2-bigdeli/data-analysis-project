-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 05, 2024 at 10:02 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `air_quality`
--

-- --------------------------------------------------------

--
-- Table structure for table `constituency`
--

CREATE TABLE `constituency` (
  `ConstituencyID` int(1) NOT NULL,
  `Name` varchar(25) DEFAULT NULL,
  `MP` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- RELATIONSHIPS FOR TABLE `constituency`:
--

-- --------------------------------------------------------

--
-- Table structure for table `measurement`
--

CREATE TABLE `measurement` (
  `MeasurementID` int(6) NOT NULL,
  `Date_Time` datetime DEFAULT NULL,
  `Site_ID` int(3) NOT NULL,
  `NOx` float DEFAULT NULL,
  `NO2` float DEFAULT NULL,
  `NO` float DEFAULT NULL,
  `PM10` float DEFAULT NULL,
  `O3` float DEFAULT NULL,
  `Temperature` float DEFAULT NULL,
  `ObjectId` int(6) DEFAULT NULL,
  `ObjectId2` int(6) DEFAULT NULL,
  `NVPM10` float DEFAULT NULL,
  `VPM10` float DEFAULT NULL,
  `NVPM2_5` float DEFAULT NULL,
  `PM2_5` float DEFAULT NULL,
  `VPM2_5` float DEFAULT NULL,
  `CO` float DEFAULT NULL,
  `RH` float DEFAULT NULL,
  `Pressure` float DEFAULT NULL,
  `SO2` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- RELATIONSHIPS FOR TABLE `measurement`:
--   `Site_ID`
--       `site` -> `SiteID`
--

-- --------------------------------------------------------

--
-- Table structure for table `schema`
--

CREATE TABLE `schema` (
  `Schema` int(2) NOT NULL,
  `Measure` varchar(25) DEFAULT NULL,
  `Description` text DEFAULT NULL,
  `Unit` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- RELATIONSHIPS FOR TABLE `schema`:
--

-- --------------------------------------------------------

--
-- Table structure for table `site`
--

CREATE TABLE `site` (
  `SiteID` int(3) NOT NULL,
  `ConstituencyID` int(1) NOT NULL,
  `Latitude` float DEFAULT NULL,
  `Longitude` float DEFAULT NULL,
  `Name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- RELATIONSHIPS FOR TABLE `site`:
--   `ConstituencyID`
--       `constituency` -> `ConstituencyID`
--

--
-- Indexes for dumped tables
--

--
-- Indexes for table `constituency`
--
ALTER TABLE `constituency`
  ADD PRIMARY KEY (`ConstituencyID`);

--
-- Indexes for table `measurement`
--
ALTER TABLE `measurement`
  ADD PRIMARY KEY (`MeasurementID`),
  ADD KEY `Site_ID` (`Site_ID`);

--
-- Indexes for table `schema`
--
ALTER TABLE `schema`
  ADD PRIMARY KEY (`Schema`);

--
-- Indexes for table `site`
--
ALTER TABLE `site`
  ADD PRIMARY KEY (`SiteID`),
  ADD KEY `ConstituencyID` (`ConstituencyID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `measurement`
--
ALTER TABLE `measurement`
  MODIFY `MeasurementID` int(6) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `schema`
--
ALTER TABLE `schema`
  MODIFY `Schema` int(2) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `measurement`
--
ALTER TABLE `measurement`
  ADD CONSTRAINT `measurement_ibfk_1` FOREIGN KEY (`Site_ID`) REFERENCES `site` (`SiteID`);

--
-- Constraints for table `site`
--
ALTER TABLE `site`
  ADD CONSTRAINT `site_ibfk_1` FOREIGN KEY (`ConstituencyID`) REFERENCES `constituency` (`ConstituencyID`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
