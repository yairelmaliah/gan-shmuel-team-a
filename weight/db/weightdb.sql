--
-- Database: `Weight`
--

CREATE DATABASE IF NOT EXISTS `weight`;

-- --------------------------------------------------------

--
-- Table structure for table `containers-registered`
--

USE weight;


CREATE TABLE IF NOT EXISTS `containers_registered` (
  `container_id` varchar(15) NOT NULL,
  `weight` int(12) DEFAULT NULL,
  `unit` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`container_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10001 ;

-- --------------------------------------------------------

--
-- Table structure for table `transactions`
--


CREATE TABLE IF NOT EXISTS `transactions` (
  `id` int(12) NOT NULL AUTO_INCREMENT,
  `datetime` datetime DEFAULT NULL,
  `direction` varchar(10) DEFAULT NULL,
  `truck` varchar(50) DEFAULT NULL,
  `containers` varchar(10000) DEFAULT NULL,
  `bruto` int(12) DEFAULT NULL,
  `truckTara` int(12) DEFAULT NULL,
  --   "neto": <int> or "na" // na if some of containers unknown
  `neto` int(12) DEFAULT NULL,
  `produce` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=10001 ;

show tables;

describe containers_registered;
describe transactions;

DROP TABLE IF EXISTS `trucks`;
CREATE TABLE `trucks` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `truckid` varchar(45) NOT NULL,
  `weight` float DEFAULT NULL,
  `unit` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO trucks (truckid,weight,unit) VALUES ('77777',666,'lbs');
INSERT INTO trucks (truckid,weight,unit) VALUES ('66666',120,'kg');
INSERT INTO trucks (truckid,weight,unit) VALUES ('99888',999,'lbs');
INSERT INTO trucks (truckid,weight,unit) VALUES ('66321',741,'kg');
INSERT INTO trucks (truckid,weight,unit) VALUES ('12365',854,'lbs');
--
-- Dumping data for table `test`
--

-- INSERT INTO `test` (`id`, `aa`) VALUES
-- (1, 'aaaa'),
