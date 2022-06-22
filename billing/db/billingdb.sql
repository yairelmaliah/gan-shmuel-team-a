--
-- Database: `billdb`
--

CREATE DATABASE IF NOT EXISTS `billdb`;
USE `billdb`;

-- --------------------------------------------------------

--
-- Table structure
--

CREATE TABLE IF NOT EXISTS `Provider` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  AUTO_INCREMENT=10001 ;

CREATE TABLE IF NOT EXISTS `Rates` (
  `product_id` varchar(50) NOT NULL,
  `rate` int(11) DEFAULT 0,
  `scope` varchar(50) DEFAULT NULL,
  FOREIGN KEY (scope) REFERENCES `Provider`(`id`)
) ENGINE=MyISAM ;

CREATE TABLE IF NOT EXISTS `Trucks` (
  `id` varchar(10) NOT NULL,
  `provider_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`provider_id`) REFERENCES `Provider`(`id`)
) ENGINE=MyISAM ;

--
-- Dumping data
--


INSERT INTO Provider (`name`) VALUES ('user1');
INSERT INTO Provider (`name`) VALUES ('user2');
INSERT INTO Provider (`name`) VALUES ('user3');
INSERT INTO Provider (`name`) VALUES ('user4');
INSERT INTO Provider (`name`) VALUES ('user5');
INSERT INTO Provider (`name`) VALUES ('user6');
INSERT INTO Provider (`name`) VALUES ('user7');
INSERT INTO Provider (`name`) VALUES ('user8');
INSERT INTO Provider (`name`) VALUES ('user9');
INSERT INTO Provider (`name`) VALUES ('user10');



INSERT INTO Trucks (`id`, `provider_id`) VALUES ('134-33-443', 10001);
INSERT INTO Trucks (`id`, `provider_id`) VALUES ('155-34-443', 10002);
INSERT INTO Trucks (`id`, `provider_id`) VALUES ('165-34-443', 10003);
INSERT INTO Trucks (`id`, `provider_id`) VALUES ('176-34-443', 10004);
INSERT INTO Trucks (`id`, `provider_id`) VALUES ('185-34-443', 10005);
INSERT INTO Trucks (`id`, `provider_id`) VALUES ('195-37-443', 10006);
INSERT INTO Trucks (`id`, `provider_id`) VALUES ('100-35-443', 10007);
INSERT INTO Trucks (`id`, `provider_id`) VALUES ('200-32-443', 10008);
INSERT INTO Trucks (`id`, `provider_id`) VALUES ('210-31-443', 10009);
INSERT INTO Trucks (`id`, `provider_id`) VALUES ('220-30-443', 10010);




INSERT INTO Rates (`product_id`, `rate`, `scope`) VALUES ('Navel', 90, 'ALL');
INSERT INTO Rates (`product_id`, `rate`, `scope`) VALUES ('Mandarin', 130, 'ALL');
INSERT INTO Rates (`product_id`, `rate`, `scope`) VALUES ('Tangerine', 90, 'ALL');
INSERT INTO Rates (`product_id`, `rate`, `scope`) VALUES ('Mandarin', 20, '45');