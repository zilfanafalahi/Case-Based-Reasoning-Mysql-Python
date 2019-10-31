-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Oct 31, 2019 at 02:03 AM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 7.3.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_cbr_python`
--

-- --------------------------------------------------------

--
-- Table structure for table `basis_kasus`
--

CREATE TABLE `basis_kasus` (
  `id` int(11) NOT NULL,
  `no_kasus` int(11) DEFAULT NULL,
  `id_penyakit` int(11) DEFAULT NULL,
  `id_gejala` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `basis_kasus`
--

INSERT INTO `basis_kasus` (`id`, `no_kasus`, `id_penyakit`, `id_gejala`) VALUES
(65, 10, 2, 6),
(64, 10, 2, 4),
(63, 9, 1, 4),
(62, 9, 1, 1),
(61, 8, 3, 9),
(60, 8, 3, 8),
(59, 8, 3, 5),
(58, 7, 1, 7),
(57, 7, 1, 3),
(56, 7, 1, 2),
(55, 6, 3, 7),
(54, 6, 3, 5),
(53, 5, 1, 5),
(52, 5, 1, 4),
(51, 5, 1, 1),
(50, 4, 4, 9),
(49, 4, 4, 8),
(48, 3, 3, 9),
(47, 3, 3, 7),
(46, 3, 3, 4),
(45, 2, 2, 4),
(44, 2, 2, 2),
(43, 1, 1, 3),
(42, 1, 1, 2),
(41, 1, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `gejala`
--

CREATE TABLE `gejala` (
  `id_gejala` int(11) NOT NULL,
  `nama_gejala` varchar(200) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `gejala`
--

INSERT INTO `gejala` (`id_gejala`, `nama_gejala`) VALUES
(1, 'G1'),
(8, 'G8'),
(7, 'G7'),
(6, 'G6'),
(5, 'G5'),
(4, 'G4'),
(3, 'G3'),
(2, 'G2'),
(9, 'G9');

-- --------------------------------------------------------

--
-- Table structure for table `penyakit`
--

CREATE TABLE `penyakit` (
  `id_penyakit` int(11) NOT NULL,
  `nama_penyakit` varchar(200) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `penyakit`
--

INSERT INTO `penyakit` (`id_penyakit`, `nama_penyakit`) VALUES
(1, 'A'),
(2, 'B'),
(4, 'D'),
(3, 'C');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `basis_kasus`
--
ALTER TABLE `basis_kasus`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `gejala`
--
ALTER TABLE `gejala`
  ADD PRIMARY KEY (`id_gejala`);

--
-- Indexes for table `penyakit`
--
ALTER TABLE `penyakit`
  ADD PRIMARY KEY (`id_penyakit`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `basis_kasus`
--
ALTER TABLE `basis_kasus`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=66;

--
-- AUTO_INCREMENT for table `gejala`
--
ALTER TABLE `gejala`
  MODIFY `id_gejala` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `penyakit`
--
ALTER TABLE `penyakit`
  MODIFY `id_penyakit` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
